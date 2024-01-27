import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import json

from getTranscripts import getVideoTransctipt
from generateArticle import *
from generatePropositon import *
from db.video import *
from db.article import *



# 配置目标video
theme = ""
videoIndex = 2


# 第一次运行，获取transcripts
with open("/Users/huangshihui/Downloads/backend/data/metadata.json") as f:
    data = json.load(f)
    video = data[theme][videoIndex]
    videoURL = video["url"]
    videoCaption = video["caption"]

getVideoTransctipt(url=videoURL, caption=videoCaption, theme=theme)




# 手动对transcripts进行切割处理，并删除sponsor等无关内容


# 第二次运行，从处理好的transcripts中生成Article和Proposition, 并插入数据库
def articleGeneration():
    # 获取分割后的transcriptsList
    transcript_path = f"/Users/huangshihui/Downloads/backend/data/raw_transcript/{theme}/{videoCaption}"
    with open(transcript_path) as f:
        transcriptPortionList = f.read.split('\n\n')
    
    for index,portion in enumerate(transcriptPortionList):

        generateArticleRawText(theme=theme, videoCaption=videoCaption, articleIndex=index)
        rawText = getArticleRawText(theme=theme, videoCaption=videoCaption, articleIndex=index)
        articleObj = getArticleObject(rawText=rawText, articleIndex=index)

        # 判断Video节点是否存在，如果不存在，则创建
        if not videoExists(url=videoURL):
            createVideo(url=videoURL, caption=videoCaption)

        # 创建Article节点，并插入数据库
        createArticle(url=videoURL, article=articleObj)

        # 为Article生成Proposition
        generatePropositionForArticle(articleObj['title'])
        


    








    







