import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
import json
from utils.translate import toChinese
from utils.path import *
from database.articleset import createArticleSet
from database.article import createArticle_insertParagraph
from database.proposition import createPropositonForParagraph

def storeArticleSet(sourceVideoURL,theme,videoTitle):

    # 获取intro
    path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
    f = open(path_intro,'r',encoding='utf-8') 
    intro = json.load(f)['content']
    f.close()

    # 获取videoTitle的中文翻译
    title_zh = toChinese(videoTitle)

    # 存储
    createArticleSet(
        sourceVideoURL=sourceVideoURL,
        theme=theme,
        title_en=videoTitle,
        title_zh=title_zh,
        intro=intro
    )
        
def storeArticle_storePararaph(sourceVideoURL,theme,videoTitle):

    articleFilePathList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)
    for path_article in articleFilePathList:
        f = open(path_article,'r',encoding='utf-8')
        fileContent = json.load(f)
        articleSequence = fileContent['metadata']['articleSequence']
        articleTitle_en = fileContent['title_en']
        articleTitle_zh = fileContent['title_zh']
        paragraphList = fileContent['paragraphList']
        createArticle_insertParagraph(sourceVideoURL=sourceVideoURL,title_en=articleTitle_en,title_zh=articleTitle_zh,paragraphs=paragraphList,sequence=articleSequence)


def storeProposition_generateEmbedding(sourceVideoURL,theme,videoTitle):

    propositionFilePathList = getPropositionFilePathList(theme=theme, videoTitle=videoTitle)
    for path_proposition in propositionFilePathList:
        f = open(path_proposition, 'r', encoding='utf-8')
        fileContent = json.load(f)
        articleSequence = fileContent['metadata']['articleSequence']
        paragraphList = fileContent['paragraphList']
        for para in paragraphList:
            paragraphSequence = para['sequence']
            propositionList = para['proposition']
            createPropositonForParagraph(sourceVideoURL=sourceVideoURL,articleSequence=articleSequence,paragraphSequence=paragraphSequence,propositionList=propositionList)



# def temp():
#     theme='The Science of Well-being'
#     videoTitle = 'How to Improve Oral Health & Its Critical Role in Brain & Body Health'
#     articleFilePathList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)
#     for path_article in articleFilePathList:
#         with open(path_article,'r+',encoding='utf-8') as f:
#             fileContent = json.load(f)
#             fileContent['title_en'] = fileContent['title']
#             fileContent['title_zh'] = toChinese(fileContent['title'])
#             del fileContent['title']
#             f.seek(0)
#             f.truncate(0)
#             f.write(json.dumps(fileContent,indent=4))


