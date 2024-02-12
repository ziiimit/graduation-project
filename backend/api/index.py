import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db.theme import getThemeArticleSetTitleList
from db.articleSet import getAllArticle,getAeticleSetTheme
from db.article import getParagraphList
from retrival.query import query

from utils.translate import toEnglish


from flask import Flask
from flask import request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

# 获取某个theme的ArticleSet列表
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


# 获取某个ArticleSet的信息，包括所属theme、标题、包含的所有文章的标题列表
@app.get("/themeArticleSet/articleSet")
def getArticleSet():

    articleSetTitle = request.args.get('title')
    # 获取as对应的theme
    theme = getAeticleSetTheme(articleSetTitle=articleSetTitle)
    themeName = theme['name']
    # 获取as的所有文章标题
    articles = getAllArticle(articleSetTitle=articleSetTitle)

    return {
        'theme':themeName,
        'title':articleSetTitle,
        "articles":articles
    }

# 获取某个文章的具体内容
@app.get("/themeArticleSet/article")
def getArticle():

    articleTitle = request.args.get('title')
    articleID = int(request.args.get('id'))
    paragraphs = getParagraphList(articleID)
    return {
        'title':articleTitle,
        "paragraphs":paragraphs
    }


# 处理用户的搜索，返回回复&推荐的文章列表
@app.get("/search")
def getSearchResult():

    userInput = request.args.get('userInput')
    userInput_en = toEnglish(userInput)
    
    return query(userInput_en)

