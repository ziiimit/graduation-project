import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
from utils.llm import translate_toEnglish,translate_toChinese
from database.retrival import getRelevantParagraphList
from utils.llm import chat
    
def generateResponse(query_en,paragraphList):

    mateirial = "Material:\n "
    for item in paragraphList:
        mateirial += item['paragraphText_en']
        mateirial += "\n"
    
    messages=[
        {"role":"system","content":"You are a professor of neurobiology and psychology with kind personality"},
        {"role":"system", "content":"Your job is generate a response to the user input based only on the material provided"},
        {"role":"system", "content":mateirial},
        {"role":"user", "content": query_en}
    ]
    
    return chat(messages=messages)



def main(query_zh):

    # 将query转化为英文（据说chat在英文上有优化，就转成英文，最后将答复转成中文）
    query_en = translate_toEnglish(query_zh)

    # 获取数据库中与query相关度大于等于relevanceRate的前upperLimit个Proposition所对应的Paragraph，
    # 及其所属的Article标题、ArticleSet标题、Theme标题
    relevanceRate = 0.65
    upperLimit = 10
    relevantParagraphList = getRelevantParagraphList(query_en=query_en,relevanceRate=relevanceRate,upperLimit=upperLimit)
    # 生成回复
    if len(relevantParagraphList) == 0:
        return{
        "paragraphList": [],
        "response_en":"Sorry, it seems like we can't find relevant article to your input",
        "response_zh":"app暂时无法找到相关文章以回复"
        }
    response_en = generateResponse(query_en=query_en, paragraphList=relevantParagraphList)
    response_zh = translate_toChinese(response_en)
    return {
        "paragraphList": relevantParagraphList,
        "response_en":response_en,
        "response_zh":response_zh
    }

# print(main("我经常睡觉前不刷牙，这对牙齿有什么危害么"))





