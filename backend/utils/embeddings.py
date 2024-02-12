import torch
from transformers import AutoModel, AutoTokenizer


# 用于生成vector的Model
# 1024维
tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-roberta-large")
model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-roberta-large")





def generateEmbeddings(target):
    inputs = tokenizer([target], padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs, output_hidden_states=True, return_dict=True).pooler_output  
    return embeddings[0].tolist()