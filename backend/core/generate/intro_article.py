import json
from openai import OpenAI
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)

# chat接口要钱，记错openAI账号注册时间，赠送的5刀用了一点点就过期了，充值要国外银行卡
# https://github.com/xing61/xiaoyi-robot?tab=readme-ov-file 可以用支付宝充值，比原价多了一点点，接口调用形式和openAI是一样的
api_key = "sk-zk29795f32167f6443e112ce116990fe14f65d1947169cd3"
base_url = "https://flag.smarttrot.com/v1/"
client = OpenAI(api_key=api_key,base_url=base_url)  # https://docs.zhizengzeng.com/ru-men/jie-kou-shi-li/mo-xing-tiao-yong-shi-li

from utils.translate import toChinese
from utils.path import *

# 生成intro, 原视频的制作风格，即先进行整个视频内容的简要介绍，本身不包含任何实质内容，对应了segments[0]
# 可以利用起来，转换为网站每一个文章series的intro
# 生成intro和生成article所需的prompt以及工作流都不太一样

# intro部分，通常包含了一些节目介绍、自我介绍，首先应该过滤掉这些内容
def filterIrrelevantContent(text, segmentTitle):

    template=f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", # 2024.2.19 gpt-3.5系列最新版本
        messages=[
            {"role":"system", "content":"Your job is to filter the content of the given text that is irrelevant to the given topic"},
            {"role":"system", "content":"Response should only contain the filtered text."},
            {"role":"user", "content":template}
        ]
    )

    return resp.choices[0].message.content


def generateIntro(text,segmentTitle):
    template=f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", 
        messages=[
            {"role":"system", "content":"Your job is to write a intro based on the given text around the given topic"},
            {"role":"system", "content":"Don't make up information that is not mentioned"},
            {"role":"system", "content":"Don't provide title, response should only contain intro itself"},
            {"role":"user", "content":template}
        ]
    )
    return resp.choices[0].message.content


def generateArticle(text,segmentTitle):

    template=f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", 
        messages=[
            {"role":"system", "content":"Your job is to write an essay based on the given text around the given topic"},
            {"role":"system", "content":"Don't make up information that is not mentioned"},
            {"role":"system", "content":"Don't provide title, response should only contain paragraphs"},
            {"role":"user", "content":template}
        ]
    )
    list = resp.choices[0].message.content.split('\n\n')
    res = []
    for i in range(len(list)):
        res.append({
            'sequence': i,
            'text_en':list[i],
            'text_zh':toChinese(list[i])
        })

    return res



def main(theme,videoTitle):
    path_transcript = getTranscriptFilePath(theme=theme,videoTitle=videoTitle)

    # 获取transcript的segments
    with open(path_transcript,'r',encoding='utf-8') as f:

        segments = json.load(f)['transcriptSegments']

        for i in range(len(segments)):

            text = segments[i]['text']
            segmentTitle = segments[i]['segmentTitle']

            # 生成intro
            if i == 0:

                filteredText = filterIrrelevantContent(text=text,segmentTitle=segmentTitle)
                intro = generateIntro(text=filteredText,segmentTitle=segmentTitle)
                
                fileContent = {
                    "metadata":{
                        'type':'intro',
                        'theme':theme,
                        'videoTitle':videoTitle
                    },
                    'title_en':segmentTitle,
                    'title_zh':toChinese(segmentTitle),
                    'content':intro
                }
                path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
                os.makedirs(os.path.dirname(path_intro), exist_ok=True)  # 父文件夹不存在则创建，存在则remain unaltered
                with open(path_intro,'w',encoding='utf-8') as f:
                    f.write(json.dumps(fileContent,indent=4))

            else:
                # 生成文章
                fileContent = {
                    "metadata":{
                        'type':'article',
                        'theme':theme,
                        'videoTitle':videoTitle,
                        'articleSequence':i-1
                    },
                    'title_en':segmentTitle,
                    'title_zh':toChinese(segmentTitle),
                    'paragraphList':generateArticle(text=text,segmentTitle=segmentTitle)
                }
                path_article = getArticleFilePath(theme=theme,videoTitle=videoTitle,fileIndex=i-1)
                with open(path_article,'w',encoding='utf-8') as f:
                    f.write(json.dumps(fileContent,indent=4))


