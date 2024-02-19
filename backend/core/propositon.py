# import sys
import json
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from openai import OpenAI



api_key = "sk-zk29795f32167f6443e112ce116990fe14f65d1947169cd3"
base_url = "https://flag.smarttrot.com/v1/"
client = OpenAI(api_key=api_key,base_url=base_url)  

# prompt出处：https://smith.langchain.com/hub/wfh/proposal-indexing?organizationId=97591f89-2916-48d3-804e-20cab23f91aa
systemPrompt = """
Decompose the "Content" into clear and simple propositions, ensuring they are interpretable out of context.
1. Split compound sentence into simple sentences. Maintain the original phrasing from the input whenever possible.
2. For any named entity that is accompanied by additional descriptive information, separate this information into its own distinct proposition.
3. Decontextualize the proposition by adding necessary modifier to nouns or entire sentences and replacing pronouns (e.g., "it", "he", "she", "they", "this", "that") with the full name of the entities they refer to.
4. Present the results as a list of strings, formatted in JSON.

Example:

Input: Title: ¯Eostre. Section: Theories and interpretations, Connection to Easter Hares. Content:\nThe earliest evidence for the Easter Hare (Osterhase) was recorded in south-west Germany in\n1678 by the professor of medicine Georg Franck von Franckenau, but it remained unknown in\nother parts of Germany until the 18th century. Scholar Richard Sermon writes that "hares were\nfrequently seen in gardens in spring, and thus may have served as a convenient explanation for the\norigin of the colored eggs hidden there for children. Alternatively, there is a European tradition\nthat hares laid eggs, since a hare’s scratch or form and a lapwing’s nest look very similar, and\nboth occur on grassland and are first seen in the spring. In the nineteenth century the influence\nof Easter cards, toys, and books was to make the Easter Hare/Rabbit popular throughout Europe.\nGerman immigrants then exported the custom to Britain and America where it evolved into the Easter Bunny."
Output: [ "The earliest evidence for the Easter Hare was recorded in south-west Germany in\n1678 by Georg Franck von Franckenau.", "Georg Franck von Franckenau was a professor of\nmedicine.", "The evidence for the Easter Hare remained unknown in other parts of Germany until\nthe 18th century.", "Richard Sermon was a scholar.", "Richard Sermon writes a hypothesis about\nthe possible explanation for the connection between hares and the tradition during Easter", "Hares\nwere frequently seen in gardens in spring.", "Hares may have served as a convenient explanation\nfor the origin of the colored eggs hidden in gardens for children.", "There is a European tradition\nthat hares laid eggs.", "A hare’s scratch or form and a lapwing’s nest look very similar.", "Both\nhares and lapwing’s nests occur on grassland and are first seen in the spring.", "In the nineteenth\ncentury the influence of Easter cards, toys, and books was to make the Easter Hare/Rabbit popular\nthroughout Europe.", "German immigrants exported the custom of the Easter Hare/Rabbit to\nBritain and America.", "The custom of the Easter Hare/Rabbit evolved into the Easter Bunny in\nBritain and America."]
"""


def generateProposition(paragraph):

    template=f"""
        'Decompose the following:\n{paragraph}'
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", 
        messages=[
            {"role":"system", "content":systemPrompt},
            {"role":"user", "content":template}
        ]
    )

    content = resp.choices[0].message.content

    # 返回的格式不是很准确，最后一个元素可能会多一个“,”不符合json数据格式
    try:
        return json.loads(content)
    except ValueError:
        print(resp.choices[0].message.content)
        temp = content.rsplit(',',1)
        res = temp[0].join(temp[1])
        return res

# ['article3.json', 'article12.json', 'article13.json', 'article2.json', 'article9.json', 'article14.json', 'article5.json', 'article18.json', 'article19.json', 'article4.json', 'article15.json', 'article8.json', 'article16.json', 'article7.json', 'article6.json', 'article17.json', 'article1.json', 'article10.json', 'article11.json', 'article0.json']

# 创建video对应的proposition文件夹和下面的所有文件
# 返回所有article的路径列表
def prepare(theme,videoTitle):

    path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
    articleFileNameList = os.listdir(path_articleDir)
    articleFileNameList.remove('intro.json')
    articleFileNameList.remove('article3.json')
    articleFileNameList.remove('article12.json')
    articleFileNameList.remove('article13.json')
    articleFileNameList.remove('article2.json')
    articleFileNameList.remove('article9.json')
    articleFileNameList.remove('article14.json')
    articleFileNameList.remove('article5.json')
    # 创建文件夹
    path_propositionDir = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}'
    os.makedirs(path_propositionDir,exist_ok=True)
    # 创建文件
    articlePropositionFilePathList = [path_propositionDir + f'/{fileName}' for fileName in articleFileNameList]
    for path in articlePropositionFilePathList:
        f = open(path,'w',encoding='utf-8')
        f.close()


    articleFilePathList = [path_articleDir + f'/{fileName}' for fileName in articleFileNameList]
    return articleFilePathList
    

    

# 获取 article 数据
def getArticle(articleFilePath):

    with open(articleFilePath,'r',encoding='utf-8') as f:
        # 获取article的元信息
        article = json.load(f)
        articleSequence = article['metadata']['articleSequence']
        paragraphList = article['paragraphList']

        return {
            'articleSequence':articleSequence,
            "paragraphList":paragraphList
        }





def main():

    theme = 'focus_productivity_and_creativity'
    videoTitle = "How to Improve Oral Health & Its Critical Role in Brain & Body Health"
    
    articleFilePathList = prepare(theme=theme,videoTitle=videoTitle)

    for articleFilePath in articleFilePathList:


        article = getArticle(articleFilePath=articleFilePath)
        articleSequence = article['articleSequence']
        paragraphList = article['paragraphList']

        for paragraph in paragraphList:
            paragraphProposition = {
                'sequence':paragraph['sequence'],
                'proposition':generateProposition(paragraph['text'])
                # 'propositionList':['hhh']
            }

            articlePropositionPath = PROJECT_ROOT + f'/data/generated_proposition/{theme}/{videoTitle}/article{articleSequence}.json'
            with open(articlePropositionPath,'r+',encoding='utf-8') as f:
                try:
                    fileContent = json.load(f)
                    fileContent['paragraphList'].append(paragraphProposition)
                    # 清空
                    f.seek(0)   
                    f.truncate(0)
                    # 重写
                    f.write(json.dumps(fileContent,indent=4))
                except ValueError: # 空文件触发
                        fileContent = {
                            'metadata':{
                                'theme':theme,
                                'videoTitle':videoTitle,
                                'articleSequence':articleSequence
                            },
                            'paragraphList':[paragraphProposition]
                        }
                        f.write(json.dumps(fileContent,indent=4))

        # break

main() 
# path = "/Users/huangshihui/Downloads/graduation-project/backend/data/generated_proposition/focus_productivity_and_creativity/How to Improve Oral Health & Its Critical Role in Brain & Body Health/article3.json"
# try:
#     with open(path,'r') as f:
#         articleProposition = json.load(f)
# except ValueError:
#     print("hi")


# theme = 'focus_productivity_and_creativity'
# videoTitle = "How to Improve Oral Health & Its Critical Role in Brain & Body Health"
   
# path_articleDir = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}'
# articleFileNameList = os.listdir(path_articleDir)
# articleFileNameList.remove('intro.json')    
# # articleFilePathList = [path_articleDir + f'/{fileName}' for fileName in articleFileNameList]

# print(articleFileNameList)

# # articleFilePath = path_articleDir + '/article4.json'
# for articleFilePath in articleFilePathList:
#     with open(articleFilePath,'r+') as f:
#             fileContent = json.load(f)
#             f.seek(0)   
#             f.truncate(0)
#             f.write(json.dumps(fileContent,indent=4))
                        
