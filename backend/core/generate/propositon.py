import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
import json
from utils.path import *
from backend.utils.dataDirReadandWrite import readArticle
from utils.llm import chat
from utils.llm import translate_toChinese

# prompt出处：https://smith.langchain.com/hub/wfh/proposal-indexing?organizationId=97591f89-2916-48d3-804e-20cab23f91aa
# 有论文
systemPrompt = """
Decompose the "Content" into clear and simple propositions, ensuring they are interpretable out of context.
1. Split compound sentence into simple sentences. Maintain the original phrasing from the input whenever possible.
2. For any named entity that is accompanied by additional descriptive information, separate this information into its own distinct proposition.
3. Decontextualize the proposition by adding necessary modifier to nouns or entire sentences and replacing pronouns (e.g., "it", "he", "she", "they", "this", "that") with the full name of the entities they refer to.
4. Present the results as a list of strings, formatted in JSON.

Example:

Input: Title: ¯Eostre. Section: Theories and interpretations, Connection to Easter Hares. Content:\nThe earliest evidence for the Easter Hare (Osterhase) was recorded in south-west Germany in\n1678 by the professor of medicine Georg Franck von Franckenau, but it remained unknown in\nother parts of Germany until the 18th century. Scholar Richard Sermon writes that "hares were\nfrequently seen in gardens in spring, and thus may have served as a convenient explanation for the\norigin of the colored eggs hidden there for children. Alternatively, there is a European tradition\nthat hares laid eggs, since a hare’s scratch or form and a lapwing’s nest look very similar, and\nboth occur on grassland and are first seen in the spring. In the nineteenth century the influence\nof Easter cards, toys, and books was to make the Easter Hare/Rabbit popular throughout Europe.\nGerman immigrants then exported the custom to Britain and America where it evolved into the Easter Bunny."
Output: [ "The earliest evidence for the Easter Hare was recorded in south-west Germany in\n1678 by Georg Franck von Franckenau.", "Georg Franck von Franckenau was a professor of\nmedicine.", "The evidence for the Easter Hare remained unknown in other parts of Germany until\nthe 18th century.", "Richard Sermon was a scholar.", "Richard Sermon writes a hypothesis about\nthe possible explanation for the connection between hares and the tradition during Easter", "Hares\nwere frequently seen in gardens in spring.", "Hares may have served as a convenient explanation\nfor the origin of the colored eggs hidden in gardens for children.", "There is a European tradition\nthat hares laid eggs.", "A hare’s scratch or form and a lapwing’s nest look very similar.", "Both\nhares and lapwing’s nests occur on grassland and are first seen in the spring.", "In the nineteenth\ncentury the influence of Easter cards, toys, and books was to make the Easter Hare/Rabbit popular\nthroughout Europe.", "German immigrants exported the custom of the Easter Hare/Rabbit to\nBritain and America.", "The custom of the Easter Hare/Rabbit evolved into the Easter Bunny in\nBritain and America."]
"""


def generateProposition(paragraph):

    template = f"""
        'Decompose the following:\n{paragraph}'
    """
    messages = [
        {"role":"system", "content":systemPrompt},
        {"role":"user", "content":template}
    ]
    content = chat(messages=messages)

    # 返回的格式不是很准确，最后一个元素可能会多一个“,”不符合json数据格式
    try:
        return json.loads(content)
    except ValueError:
        temp = content.rsplit(',',1)
        res = temp[0].join(temp[1])
        return res



def main(theme, videoTitle):

    articleFilePathList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)

    for articleSequence in range(len(articleFilePathList)):

        # 文件不存在则创建，存在则保持原状
        path_propositionFile = getPropositionFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        f = open(path_propositionFile,'a',encoding='utf-8')
        f.close()

        article = readArticle(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        paragraphList = article['paragraphList']


        for paragraph in paragraphList:

            # 获取数据
            paragraphProposition = {
                'sequence':paragraph['sequence'],
                'proposition':generateProposition(paragraph['text_en'])
            }

            # 写入文件
            with open(path_propositionFile,'r+',encoding='utf-8') as f:
                try:
                    fileContent = json.load(f)
                    fileContent['paragraphList'].append(paragraphProposition)
                    # 清空
                    f.seek(0)   
                    f.truncate(0)
                    # 重写
                    f.write(json.dumps(fileContent,indent=4))
                except ValueError: # 空文件触发
                        fileContent = {
                            'meta':{
                                'theme':theme,
                                'videoTitle':videoTitle,
                                'articleSequence':articleSequence
                            },
                            'paragraphList':[paragraphProposition]
                        }
                        f.write(json.dumps(fileContent,indent=4))



                  
