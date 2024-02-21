import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))



def getTranscriptFilePath(theme,videoTitle):
    return PROJECT_ROOT + f'/data/raw_transcript/{theme}/{videoTitle}.json'

def getArticleDirPath(theme,videoTitle):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    return path_articleDir

def getArticleFilePathList(theme,videoTitle,removeList=[]):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    articleFileNameList = os.listdir(path_articleDir)
    articleFileNameList.remove('intro.json')
    for item in removeList:
        articleFileNameList.remove(item)
    articleFilePathList = [path_articleDir + f'/{fileName}' for fileName in articleFileNameList]

    return articleFilePathList


def getArticleFilePath(theme,videoTitle,fileIndex):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    return path_articleDir + f'/article{fileIndex}.json'


def getIntroFilePath(theme,videoTitle):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    return path_articleDir + '/intro.json'


def getPropositionDirPath(theme,videoTitle):
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    return path_propositionDir



def getPropositionFilePathList(theme,videoTitle):
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    propositionFileNameList = os.listdir(path_propositionDir)
    propositionFilePathList = [path_propositionDir + f'/{fileName}' for fileName in propositionFileNameList]
    return propositionFilePathList


