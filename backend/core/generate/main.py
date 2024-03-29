from transcript import main as transcript_main
from intro_article import main as intro_article_main
from propositon import main as proposition_main
from summary import main as summary_main


from utils.dataDirReadandWrite import readSingleMeta,appendMeta
from utils.path import *
from db.index import *



# 创建article和proposition的文件夹，transcript和summary由于是一个文件涵盖全部，不存在文件夹
def prepareDir(theme,videoTitle):
    path_articleDir = getArticleDirPath(theme=theme, videoTitle=videoTitle)
    path_propositionDir = getPropositionDirPath(theme=theme,videoTitle=videoTitle)
    os.makedirs(path_articleDir, exist_ok=True) 
    os.makedirs(path_propositionDir, exist_ok=True) 
    
themes = [
    "Mental Health and Addiction",
   "Focus, Productivity and Creativity",
    "The Science of Well-being"
]


def main(videoURL,theme): 

    # 获取transcripts并存储至项目文件夹下，将videoTitle添加到meta中
    abandonList = ['sponsor','office time', 'podcast'
                   'ag1','athletic greens','Announcement: Spanish Subtitles',"Surprise!","Huberman",
                   "Notes About Spanish Captions","Announcing New Cost-Free Resources",
                   "Roundup, Various Forms of Support","Closing Remarks"]
    videoTitle = transcript_main(videoURL=videoURL,theme=theme,abandonList=abandonList)
    appendMeta(videoURL=videoURL,theme=theme,videoTitle=videoTitle)
    videoTitle = readSingleMeta()['videoTitle']
    prepareDir(theme=theme,videoTitle=videoTitle)

    intro_article_main(theme=theme,videoTitle=videoTitle)

    summary_main(theme=theme,videoTitle=videoTitle)

    proposition_main(theme=theme,videoTitle=videoTitle,startFrom=17)

    loadFromDataDirToDatabase()


def loadAllFromDataDirToDatabase():
    metaList = readAllMeta()
    for meta in metaList[1:]:
        videoTitle = meta['videoTitle']
        theme=meta['theme']
        print(f"current: {videoTitle}")
        # videoURL = meta['videoURL']
        # storeArticleSet(sourceVideoURL=videoURL,videoTitle=videoTitle,theme=theme)
        # storeArticle_storePararaph(videoTitle=videoTitle,theme=theme)
        # storeSummary(theme=theme,videoTitle=videoTitle)   
        storeProposition_generateEmbedding(videoTitle=videoTitle,theme=theme)



loadAllFromDataDirToDatabase()