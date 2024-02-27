import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
from utils.path import *
from utils.dataDirReadandWrite import readArticle,appendSummary
from utils.llm import chat,translate_toChinese


def generateSummary(theme,text):

    tone = {
        "Focus, Productivity and Creativity":"educational",
        "Mental Health and Addiction":"educational",
        "The Science of Well-being":"humorous"
    }

    messages = [
        {"role":"system", "content":"Your job is to generate an appealing intro of the given article."},
        {"role":"system", "content":f"Your tone should be {tone[theme]}."},
        {"role":"system", "content":"Response should only contain the summary itself."},
        {"role":"user", "content":f"Article:\n{text}"}
    ]
    content = chat(messages=messages)

    return content



            

def main(theme,videoTitle,startFrom=0):
    print(f"generating summary, start from article{startFrom}")
    # 读取article的内容
    path_articleList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)
    for articleSequence in range(startFrom,len(path_articleList)):
        print(f"start article{articleSequence}")
        article =readArticle(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        paragraphList = article['paragraphList']
        text = ""
        for para in paragraphList:
            text += para['text_en']
            text += '\n'
        summary_en = generateSummary(text=text,theme=theme)
        summary_zh = translate_toChinese(summary_en)
        print(f"append")
        appendSummary(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence,summary_en=summary_en,summary_zh=summary_zh)


    

