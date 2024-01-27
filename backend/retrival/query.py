import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import torch
from scipy.spatial.distance import cosine
from transformers import AutoModel, AutoTokenizer
from db.proposition import findSimilarPropositions,getCorrespondingParagraph


# 用于生成vector的Model
# 1024
tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-roberta-large")
model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-roberta-large")


def query(query):

    inputs = tokenizer([query], padding=True, truncation=True, return_tensors="pt")

    with torch.no_grad():
        embeddings = model(**inputs, output_hidden_states=True, return_dict=True).pooler_output  
    
    similarPropositions = findSimilarPropositions(queryEmbedding=embeddings[0].tolist(), num=5)

    paraList = []

    for item in similarPropositions:

        result = getCorrespondingParagraph(item['id'])

        alreadyHas = False
        for para in paraList:
            if para['id'] == result['id']:
                alreadyHas = True
                break

        if not alreadyHas:
            paraList.append(result)

    str = ""
    for item in paraList:
        str += item['content']
        str += '\n'


    print(str)



query("i can't stop eating, what's wrong with me")