import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)
from utils.path import *
import json

# meta
    # 读取meta中的第index个元素
def readMeta(index=-1):
    path_meta = getMetaFilePath()
    f = open(path_meta, 'r',encoding='utf-8')
    fileContent = json.load(f)
    f.close()
    return fileContent[index]
    # 向meta中的第index元素中添加爬取的videoTitle属性
def appendMeta(videoURL,theme,videoTitle):
    path_meta = getMetaFilePath()
    f = open(path_meta, 'r+',encoding='utf-8')
    fileContent = json.load(f)
    fileContent.append({
        "videoTitle":videoTitle,
        "videoURL":videoURL,
        "theme" :theme
    })
    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(fileContent,indent=4))
    f.close()

# transcript
    # 读取transcript文件中的所有内容，并转换为json
def readTranscript(theme,videoTitle):
    path_transcript = getTranscriptFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_transcript,'r',encoding='utf-8') as f:
        return json.load(f)
    # 写文件，一个transcripts调用一次，一次写全部
def writeTranscript(theme,videoTitle,fileContent):
    path_transcript = getTranscriptFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_transcript,"w",encoding="utf-8") as f:
        f.write(json.dumps(fileContent,indent=4))

# generated_article
    # 读文件的所有内容
def readIntro(theme,videoTitle):
    path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_intro,'r',encoding='utf-8') as f:
        return json.load(f)
    # 写文件，一个intro调一次，一次写全部
def writeIntro(theme,videoTitle,fileContent):
    path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_intro,'w',encoding='utf-8') as f:
        f.write(json.dumps(fileContent,indent=4))

    # 读文件的所有内容
def readArticle(theme,videoTitle,articleSequence):
    path_article = getArticleFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    with open(path_article,'r',encoding='utf-8') as f:
        return json.load(f)
    # 写文件，一个article调一次，一次写全部
def writeArticle(theme,videoTitle,articleSequence,fileContent):
    path_article = getArticleFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    with open(path_article,'w',encoding='utf-8') as f:
        f.write(json.dumps(fileContent,indent=4))
    


# generated_proposition
    # 读文件的所有内容
def readProposition(theme,videoTitle,articleSequence):
    path_proposition = getPropositionFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    with open(path_proposition,'r',encoding='utf-8') as f:
        return json.load(f)
    
    # 写文件，一个article调用len(paragraphList)次
    # 先读，后append，再覆盖
    # 需区分初次写和非初次写
def appendProposition(theme,videoTitle,articleSequence,proposition):

    # 文件不存在则创建，存在则保持原状
    path_propositionFile = getPropositionFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    f = open(path_propositionFile,'a',encoding='utf-8')
    f.close()

    with open(path_propositionFile,'r+',encoding='utf-8') as f:
        try:
            fileContent = json.load(f)
            fileContent['paragraphList'].append(proposition)
            # 清空
            f.seek(0)   
            f.truncate(0)
            # 覆盖
            f.write(json.dumps(fileContent,indent=4))
        except ValueError: # 空文件触发
            fileContent = {
                'meta':{
                    'theme':theme,
                    'videoTitle':videoTitle,
                    'articleSequence':articleSequence
                },
                'paragraphList':[proposition]
            }
            f.write(json.dumps(fileContent,indent=4))
    # 清除文件内容
def clearPropositionFile(theme,videoTitle,articleSequence):
    # 文件不存在则创建，存在则保持原状
    path_propositionFile = getPropositionFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    f = open(path_propositionFile,'w',encoding='utf-8')
    f.close()


# summary
    # 读文件的所有内容
def readSummaryList(theme,videoTitle):
    path_summary = getSummaryFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_summary,'r',encoding='utf-8') as f:
        return json.load(f)
    
    # 写文件，一个articleSet的每个article都调用一次
    # 先读，后append，再覆盖
    # 需区分初次写和非初次写
def appendSummary(theme,videoTitle,articleSequence,summary_en,summary_zh):
    path_summary = getSummaryFilePath(theme=theme,videoTitle=videoTitle)
    # 没有文件则创建
    f = open(path_summary,'a',encoding='utf-8')
    f.close()
    # 写文件
    with open(path_summary,'r+',encoding='utf-8') as f:
        try:
            fileContent = json.load(f)
            fileContent.append({
                "articleSequence":articleSequence,
                "summary_en":summary_en,
                "summary_zh":summary_zh
            })
            f.seek(0)
            f.truncate(0)
            f.write(json.dumps(fileContent,indent=4))
        except ValueError: # 空文件
            fileContent = [
                {
                    "articleSequence":articleSequence,
                    "summary_en":summary_en,
                    "summary_zh":summary_zh
                }
            ]
            f.write(json.dumps(fileContent,indent=4))