import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)
from utils.path import *
import json

# meta
def readMetaByIndex(index):
    path_meta = getMetaFilePath()
    f = open(path_meta, 'r',encoding='utf-8')
    fileContent = json.load(f)
    f.close()
    return fileContent[index]

def writeMetaVideoTitle(index,videoTitle):
    path_meta = getMetaFilePath()
    f = open(path_meta, 'r+',encoding='utf-8')
    fileContent = json.load(f)
    fileContent[index]['videoTitle'] = videoTitle
    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(fileContent,indent=4))
    f.close()

# transcript
def readTranscript(theme,videoTitle):
    path_transcript = getTranscriptFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_transcript,'r',encoding='utf-8') as f:
        return json.load(f)


# generated_article
def readIntro(theme,videoTitle):
    path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_intro,'r',encoding='utf-8') as f:
        return json.load(f)

def readArticle(theme,videoTitle,articleSequence):
    path_article = getArticleFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    with open(path_article,'r',encoding='utf-8') as f:
        return json.load(f)
    
# generated_proposition
def readProposition(theme,videoTitle,articleSequence):
    path_proposition = getPropositionFilePath(theme=theme,videoTitle=videoTitle,articleSequence=articleSequence)
    with open(path_proposition,'r',encoding='utf-8') as f:
        return json.load(f)

# summary
def readSummaryList(theme,videoTitle):
    path_summary = getSummaryFilePath(theme=theme,videoTitle=videoTitle)
    with open(path_summary,'r',encoding='utf-8') as f:
        return json.load(f)