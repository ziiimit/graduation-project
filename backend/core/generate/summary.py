import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
import json
from utils.path import *
from utils.dataDirReadandWrite import readArticle
from utils.llm import chat,translate_toChinese


def generateSummary(theme,text):

    tone = {
        "Focus, Productivity and Creativity":"educational",
        "Mental Health and Addiction":"educational",
        "The Science of Well-being":"humorous"
    }

    messages = [
        {"role":"system", "content":"Your job is to generate an appealing intro of the given article."},
        {"role":"system", "content":f"Your tone should be {tone['theme']}."},
        {"role":"system", "content":"Response should only contain the summary itself."},
        {"role":"user", "content":f"Article:\n{text}"}
    ]
    content = chat(messages=messages)

    return content


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
        except: # 空文件
            fileContent = [
                {
                    "articleSequence":articleSequence,
                    "summary_en":summary_en,
                    "summary_zh":summary_zh
                }
            ]
            f.write(json.dumps(fileContent,indent=4))
            

def main(theme,videoTitle):

    # 读取article的内容
    path_articleList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)
    for articleSequence in range(len(path_articleList)):
        article =readArticle(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        paragraphList = article['paragraphList']
        text = ""
        for para in paragraphList:
            text += para['text_en']
            text += '\n'
        summary_en = generateSummary(text=text)
        summary_zh = translate_toChinese(summary_en)
        appendSummary(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence,summary_en=summary_en,summary_zh=summary_zh)


    

