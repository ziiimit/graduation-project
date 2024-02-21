# 下面4句是配置路径，为了能够正确导入db中的函数
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))



from utils.embeddings import generateEmbedding
from db.proposition import *




def generateArticlePropositionsVector(articleTitle):

    propositionList = getArticlePropositions(articleTitle)

    result = []

    for proposition in propositionList:

        if(hasEmbedding(proposition)):
            continue

        proposition['embedding'] = generateEmbedding(proposition["content"])
        result.append(proposition)
        
    setPropositionsEmbedding(result)









