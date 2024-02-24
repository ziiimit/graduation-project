import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from database.articleset import getArticleSetList,getArticleSet
from database.article import getArticle
from utils.llm import translate_toEnglish


from flask import Flask
from flask import request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

# 获取某个theme的ArticleSet列表
@app.get("/articleSetList")
def articleSetList():

    themeTitle_en = request.args.get('themeTitle_en')
    res = getArticleSetList(themeTitle_en)

    return res

# 获取某个ArticleSet的Article列表
@app.get("/articleSet")
def articleSet():

    articleSetTitle_en = request.args.get('articleSetTitle_en')
    res = getArticleSet(articleSetTitle_en=articleSetTitle_en)

    return res



# 获取某个Article
@app.get("/article")
def article():

    articleSetTitle_en = request.args.get('articleSetTitle_en')
    articleSequence = request.args.get('articleSequence')
    res = getArticle(articleSetTitle_en=articleSetTitle_en,articleSequence=articleSequence)

    return res


