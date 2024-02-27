import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(PROJECT_ROOT)
import json
from utils.dataDirReadandWrite import *
from utils.path import *
from utils.llm import translate_toChinese
from database.articleset import createArticleSet
from database.article import createArticle_insertParagraph,insertSummary
from database.proposition import createPropositonForParagraph


def storeArticleSet(sourceVideoURL,theme,videoTitle):
    print("storing article set")

    # 获取intro
    intro = readIntro(
        theme=theme,
        videoTitle=videoTitle
    )
    # 获取videoTitle的中文翻译
    title_zh = translate_toChinese(videoTitle)

    # 存储
    createArticleSet(
        sourceVideoURL=sourceVideoURL,
        theme=theme,
        title_en=videoTitle,
        title_zh=title_zh,
        intro_en=intro['text_en'],
        intro_zh = intro['text_zh']
    )
        
def storeArticle_storePararaph(theme,videoTitle):

    print('storing article')
    articleFilePathList = getArticleFilePathList(theme=theme,videoTitle=videoTitle)
    for articleSequence in range(len(articleFilePathList)):
        print(f"--article{articleSequence}")
        article = readArticle(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        articleTitle_en = article['title_en']
        articleTitle_zh = article['title_zh']
        paragraphList = article['paragraphList']
        createArticle_insertParagraph(videoTitle=videoTitle,title_en=articleTitle_en,title_zh=articleTitle_zh,paragraphs=paragraphList,sequence=articleSequence)

def storeProposition_generateEmbedding(theme,videoTitle):
    print('storing proposition')
    propositionFilePathList = getPropositionFilePathList(theme=theme, videoTitle=videoTitle)
    for articleSequence in range(len(propositionFilePathList)):
        print(f"--article{articleSequence}")
        proposition = readProposition(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
        paragraphList = proposition['paragraphList']
        for para in paragraphList:
            paragraphSequence = para['sequence']
            print(f"----paragraph{paragraphSequence}")
            propositionList = para['proposition']
            createPropositonForParagraph(videoTitle=videoTitle,articleSequence=articleSequence,paragraphSequence=paragraphSequence,propositionList=propositionList)

def storeSummary(theme,videoTitle):
    print('storing summary')
    summaryList = readSummaryList(theme=theme,videoTitle=videoTitle)
    for item in summaryList:
        articleSequence = item['articleSequence']
        print(f"--article{articleSequence}")
        summary_en = item['summary_en']
        summary_zh = item['summary_zh']
        insertSummary(videoTitle=videoTitle,articleSequence=articleSequence,summary_en=summary_en,summary_zh=summary_zh)




