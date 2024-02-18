import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import json

from backend.article_generation.transcript import getTranscript
from generateArticle import *
from generatePropositon import *
from db.articleSet import *
from db.article import *



# 配置目标articleSet
theme = ""
articleSetIndex = 2


# 第一次运行，获取transcripts
with open("/Users/huangshihui/Downloads/backend/data/metadata.json") as f:
    data = json.load(f)
    articleSet = data[theme][articleSetIndex]
    articleSetURL = articleSet["url"]
    articleSetCaption = articleSet["title"]

getTranscript(url=articleSetURL, title=articleSetCaption, theme=theme)




# 手动对transcripts进行切割处理，并删除sponsor等无关内容


# 第二次运行，从处理好的transcripts中生成Article和Proposition, 并插入数据库
def articleGeneration():
    # 获取分割后的transcriptsList
    transcript_path = f"/Users/huangshihui/Downloads/backend/data/raw_transcript/{theme}/{articleSetCaption}"
    with open(transcript_path) as f:
        transcriptPortionList = f.read.split('\n\n')
    
    for index,portion in enumerate(transcriptPortionList):

        generateArticleRawText(theme=theme, articleSetCaption=articleSetCaption, articleIndex=index)
        rawText = getArticleRawText(theme=theme, articleSetCaption=articleSetCaption, articleIndex=index)
        articleObj = getArticleObject(rawText=rawText, articleIndex=index)

        # 判断ArticleSet节点是否存在，如果不存在，则创建
        if not articleSetExists(url=articleSetURL):
            createArticleSet(url=articleSetURL, title=articleSetCaption)

        # 创建Article节点，并插入数据库
        createArticle(url=articleSetURL, article=articleObj)

        # 为Article生成Proposition
        generatePropositionForArticle(articleObj['title'])
        


    








    







