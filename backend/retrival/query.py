# 下面4句是配置路径，为了能够正确导入db中的函数
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.embeddings import generateEmbedding
from utils.llm import translate_toChinese 


from db.proposition import findSimilarPropositions,getCorrespondingParagraph
from db.article import getArticleByParagraphID
from db.articleSet import getArticleSetTitleByArticleID
from db.theme import getThemeNameByArticleSetTitle



from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
openai_api_key = "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"
MODEL = OpenAI(openai_api_key=openai_api_key, temperature=0)

def generateResponse(corpus,userInput_en):
   prompt = PromptTemplate(
      template="""
        You are a kind and professional psychologist.
        Your task is to write a response to the user input based on the material provided.

        User input : {userInput_en}

        Material: {corpus}
        
        Response:
        """,
        input_variables=['corpus','userInput_en'],
    )
   
   chain = prompt | MODEL 

   response_en = chain.invoke({'corpus':corpus,'userInput_en':userInput_en})
   print(response_en)
   response_zh = translate_toChinese(queryString=response_en)
   return response_zh


def query(userInput_en):

    # 找到数据库中和用户输入的cosine-similarity值最大的前5个proposition 
    queryEmbedding = generateEmbedding(userInput_en)
    similarPropositions = findSimilarPropositions(queryEmbedding=queryEmbedding, num=5)

    # 获取proposition对应的paragraph，用于传入llm生成对用户的回答
    # 同时将paragraph对应的article找到，作为recommendedArticles返回
    paraList = []
    recommendedArticleList = []   
    for proposition in similarPropositions:

        # 根据proposition的id，找到其所属的paragraph
        paragraph = getCorrespondingParagraph(proposition['id'])

        # 如果当前proposition对应的段落已被放入paraList，则跳过，防止重复
        paraAlreadyExists = False
        for para in paraList:
            if para['id'] == paragraph['id']:
                paraAlreadyExists = True
                break
        if not paraAlreadyExists:
            # 将para添加至List
            paraList.append(paragraph)

            # 根据para的信息找到对应的article、articleSet、theme的相关信息
            article = getArticleByParagraphID(paragraph['id'])
            articleAlreadyExists = False
            for recommendedArticle in recommendedArticleList:
                if recommendedArticle['id'] == article['id']:
                    articleAlreadyExists = True
                    break
            if not articleAlreadyExists:
                articleSetTitle = getArticleSetTitleByArticleID(articleID=article['id'])
                themeName = getThemeNameByArticleSetTitle(articleSetTitle=articleSetTitle)
                recommendedArticle = {'title': article['title'],'id':article['id'],"sequence":article['sequence'],'articleSet':articleSetTitle,'theme':themeName}
                recommendedArticleList.append(recommendedArticle)


    # 将所有paragraph拼接，让llm基于此来生成对userInput的回复
    corpus = ""
    for para in paraList:
        corpus += para['content']
        corpus += '\n'
    response_zh = generateResponse(corpus=corpus, userInput_en=userInput_en)

    return {'response':response_zh,'recommendedArticleList':recommendedArticleList}

    
    

