import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import torch
from scipy.spatial.distance import cosine
from transformers import AutoModel, AutoTokenizer
from db.proposition import *
from db.article import getAllArticleTitle


# 用于生成vector的Model
# 1024
tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-roberta-large")
model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-roberta-large")




def generateVector(articleTitle):

    propositions = getArticlePropositions(articleTitle)

    print(articleTitle)

    result = []
    for item in propositions:

        if(hasEmbedding(item)):
            # print("skip",item)
            continue

        input = tokenizer([item["content"]], padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            embedding = model(**input, output_hidden_states=True).pooler_output

        item['embedding'] = embedding[0].tolist()
        result.append(item)
        
    setPropositionsEmbedding(result)





titles = getAllArticleTitle()
for title in titles:
    generateVector(title)







