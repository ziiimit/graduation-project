from generate.transcript import main as transcript_main
from generate.intro_article import main as intro_article_main
from generate.propositon import main as proposition_main


from db.index import *


def main():

    # 当前正在处理的视频
    videoURL = "https://www.youtube.com/watch?v=nm1TxQj9IsQ"
    theme = 'The Science of Well-being'

    # 获取transcripts并处理，存储至项目文件夹下
    videoTitle = transcript_main(videoURL=videoURL,theme=theme)
    print(videoTitle)
    # videoTitle = "How to Improve Oral Health & Its Critical Role in Brain & Body Health"
    # 生成intro&article
    # intro_article_main(theme=theme,videoTitle=videoTitle)
    # 在数据库内创建ArticleSet
    storeArticleSet(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)
    # 在数据库内创建Article和Paragraph
    storeArticle_storePararaph(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)
    # 生成proposition
    # proposition_main(theme=theme,videoTitle=videoTitle)
    # 存储proposition, 并生成embedding
    storeProposition_generateEmbedding(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)

    
main()