import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import time

from db.article import getAllArticleTitle, addPropositionsToParagraph, hasPropositions,getParagraphList
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain import hub


openai_api_key = "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"



def generatePropositionForArticle(articleTitle):

    paragraphList = getParagraphList(articleTitle)

    prompt = hub.pull('wfh/proposal-indexing')
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
    runnable = prompt | llm

    count = 0

    for paragraph in paragraphList:

        sequence = paragraph['sequence']
        content = paragraph['content']


        if hasPropositions(articleTitle=articleTitle, paragraphSequence=sequence):
            print("pass", sequence)
            continue


        result  = runnable.invoke({
            "input":content
        })

        # api调用的speed limit，每分钟不可以超过3个
        count += 1
        if count==3 :   
             time.sleep(60) 

        print(sequence,result.content)

        # 将字符串转化为list
        propositionList = result.content
        propositionList = propositionList.removeprefix('[\n').removesuffix('\n]').split(',\n')
        propositionList = [item.removeprefix('"').removesuffix('"') for item in propositionList]

        addPropositionsToParagraph(articleTitle=articleTitle, paragraphSequence=sequence, propositionList=propositionList)


# generatePropositionForArticle("Understanding anorexia nervosa")
titleList = getAllArticleTitle()
for title in titleList:
    generatePropositionForArticle(title)


