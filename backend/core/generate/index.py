from transcript import main as transcript_main
from intro_article import main as intro_article_main
from propositon import main as proposition_main
from summary import main as summary_main


from utils.dataDirReadandWrite import readMetaByIndex,writeMetaVideoTitle
from utils.path import *
from db.index import *

def prepareDir(theme,videoTitle):
    # 父文件夹不存在则创建，存在则remain unaltered
    path_articleDir = getArticleDirPath(theme=theme, videoTitle=videoTitle)
    path_propositionDir = getPropositionDirPath(theme=theme,videoTitle=videoTitle)
    os.makedirs(path_articleDir, exist_ok=True) 
    os.makedirs(path_propositionDir, exist_ok=True) 
    


def main(index):

    # 当前正在处理的视频
    meta = readMetaByIndex(index)
    videoURL = meta['videoURL']
    theme = meta['theme']

    # 获取transcripts并存储至项目文件夹下，将videoTitle添加到meta中
    # videoTitle = transcript_main(videoURL=videoURL,theme=theme)
    # writeMetaVideoTitle(index=index,videoTitle=videoTitle)
    videoTitle = readMetaByIndex(index=index)['videoTitle']

    # 创建article和proposition的文件夹，transcript和summary由于是一个文件涵盖全部，不存在文件夹
    prepareDir(theme=theme,videoTitle=videoTitle)

    # intro_article_main(theme=theme,videoTitle=videoTitle)
    # storeArticleSet(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)
    # storeArticle_storePararaph(videoTitle=videoTitle,theme=theme)
    
    # proposition_main(theme=theme,videoTitle=videoTitle)
    # storeProposition_generateEmbedding(videoTitle=videoTitle,theme=theme)

    # summary_main(theme=theme,videoTitle=videoTitle)
    # storeSummary(theme=theme,videoTitle=videoTitle)

    
main(2)

