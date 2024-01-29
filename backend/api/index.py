import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db.theme import getThemeArticleSetTitleList
from db.articleSet import getAllArticle,getAeticleSetTheme
from db.article import getParagraphList

from flask import Flask
from flask import request
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.get("/themeArticleSet/articleSetList")
def getArticleSetList():

    themeName = request.args.get('themeName')
    articleSetTitleList = getThemeArticleSetTitleList(themeName)

    result = []
    for articleSetTitle in articleSetTitleList:
        articleTotal = len(getAllArticle(articleSetTitle=articleSetTitle))
        result.append({
            "title": articleSetTitle,
            "articleTotal":articleTotal
        })

    return result


@app.get("/themeArticleSet/articleSet")
def getArticleSet():

    articleSetTitle = request.args.get('title')
    # 获取as对应的theme
    theme = getAeticleSetTheme(articleSetTitle=articleSetTitle)
    themeName = theme['name']
    # 获取as的所有文章
    articles = getAllArticle(articleSetTitle=articleSetTitle)

    return {
        'theme':themeName,
        'title':articleSetTitle,
        "articles":articles
    }

@app.get("/themeArticleSet/article")
def getArticle():

    articleTitle = request.args.get('title')
    articleID = int(request.args.get('id'))
    paragraphs = getParagraphList(articleID)
    print(paragraphs)
    return {
        'title':articleTitle,
        "paragraphs":paragraphs
    }


