from transcript import main as transcript_main
from intro_article import main as intro_article_main
from propositon import main as proposition_main


from db.index import *


def main(current):

    # 当前正在处理的视频
    path_meta = "/Users/huangshihui/Downloads/graduation-project/backend/data/meta.json"
    f = open(path_meta, 'r')
    meta = json.load(f)[current]
    videoURL = meta['videoURL']
    theme = meta['theme']


    # 获取transcripts并处理，存储至项目文件夹下
    # videoTitle = transcript_main(videoURL=videoURL,theme=theme)
    # print(videoTitle)

    videoTitle = "How to Increase Motivation & Drive"

    # 生成intro&article
    # intro_article_main(theme=theme,videoTitle=videoTitle)

    # 在数据库内创建ArticleSet
    # storeArticleSet(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)

    # 在数据库内创建Article和Paragraph
    # storeArticle_storePararaph(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)
    
    # 生成proposition
    # proposition_main(theme=theme,videoTitle=videoTitle)

    # 存储proposition, 并生成和存储embedding
    storeProposition_generateEmbedding(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)

    
main(2)

