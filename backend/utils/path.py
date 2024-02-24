import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# meta.py
def getMetaFilePath():
    return PROJECT_ROOT + '/data/meta.json'

# transcript
def getTranscriptDirPath(theme):
    return PROJECT_ROOT + f'/data/raw_transcript/{theme}'


def getTranscriptFilePath(theme,videoTitle):
    return PROJECT_ROOT + f'/data/raw_transcript/{theme}/{videoTitle}.json'

# generated_article
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


def getArticleFilePath(theme,videoTitle,articleSequence):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    return path_articleDir + f'/article{articleSequence}.json'


def getIntroFilePath(theme,videoTitle):
    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    return path_articleDir + '/intro.json'


# generated_proposition
def getPropositionDirPath(theme,videoTitle):
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    return path_propositionDir

def getPropositionFilePath(theme,videoTitle,articleSequence):
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    return  path_propositionDir + f'/article{articleSequence}.json'



def getPropositionFilePathList(theme,videoTitle):
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    propositionFileNameList = os.listdir(path_propositionDir)
    propositionFilePathList = [path_propositionDir + f'/{fileName}' for fileName in propositionFileNameList]
    return propositionFilePathList


# generated_summary
def getSummaryFilePath(theme,videoTitle):
    return PROJECT_ROOT + f'/data/generated_summary/{theme}/{videoTitle}.json'



