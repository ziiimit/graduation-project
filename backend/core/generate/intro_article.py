import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
import json
from utils.path import *
from backend.utils.dataDirReadandWrite import readTranscript
from utils.llm import chat
from utils.llm import translate_toChinese

# 生成intro, 原视频的制作风格，即先进行整个视频内容的简要介绍，本身不包含任何实质内容，对应了segments[0]
# 可以利用起来，转换为网站每一个文章series的intro
# 生成intro和生成article所需的prompt以及工作流都不太一样

# intro部分，通常包含了一些节目介绍、自我介绍，首先应该过滤掉这些内容
def filterIrrelevantContent(text, segmentTitle):

    template = f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    messages=[
        {"role":"system", "content":"Your job is to filter the content of the given text that is irrelevant to the given topic"},
        {"role":"system", "content":"Response should only contain the filtered text."},
        {"role":"user", "content":template}
    ]

    return chat(messages=messages)


def generateIntro(text,segmentTitle,videoTitle):
    template=f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    messages=[
        {"role":"system", "content":"Your job is to write a intro of an essay based on the given text around the given topic"},
        {"role":"system", "content":f"Don't mention Huberman Lab Podcast and focus on the topic of {videoTitle}"},
        {"role":"system", "content":"Don't provide title, response should only contain intro itself"},
        {"role":"user", "content":template}
    ]
    return chat(messages=messages)


def generateArticle(text,segmentTitle):

    template=f"""
        Topic: {segmentTitle}
        Text:{text}
    """
    messages=[
        {"role":"system", "content":"Your job is to write an essay based on the given text around the given topic"},
        {"role":"system", "content":"Preserve the explantory context, make sure the essay is detailed and can be understood by a high school student"},
        {"role":"system", "content":"Don't make up information that is not mentioned"},
        {"role":"system", "content":"Don't provide title, response should only contain paragraphs"},
        {"role":"user", "content":template}
    ]
    list = chat(messages=messages).split('\n\n')
    res = []
    for i in range(len(list)):
        res.append({
            'sequence': i,
            'text_en':list[i],
            'text_zh':translate_toChinese(list[i])
        })

    return res



def main(theme,videoTitle):

    # 获取transcript的segments
    segments = readTranscript(theme=theme,videoTitle=videoTitle)['transcriptSegments']

    for i in range(len(segments)):
            
            text = segments[i]['text']
            segmentTitle = segments[i]['segmentTitle']

            # 生成intro
            if i == 0:

                filteredText = filterIrrelevantContent(text=text,segmentTitle=segmentTitle)
                intro = generateIntro(text=filteredText,segmentTitle=segmentTitle,videoTitle=videoTitle)
                
                fileContent = {
                    "meta":{
                        'type':'intro',
                        'theme':theme,
                        'videoTitle':videoTitle,
                    },
                    'text_en':intro,
                    "text_zh":translate_toChinese(intro)
                }
                path_intro = getIntroFilePath(theme=theme,videoTitle=videoTitle)
                with open(path_intro,'w',encoding='utf-8') as f:
                    f.write(json.dumps(fileContent,indent=4))

            else:
                # 生成文章
                fileContent = {
                    "meta":{
                        'type':'article',
                        'theme':theme,
                        'videoTitle':videoTitle,
                        'articleSequence':i-1
                    },
                    'title_en':segmentTitle,
                    'title_zh':translate_toChinese(segmentTitle),
                    'paragraphList':generateArticle(text=text,segmentTitle=segmentTitle)
                }
                path_article = getArticleFilePath(theme=theme,videoTitle=videoTitle,fileIndex=i-1)
                with open(path_article,'w',encoding='utf-8') as f:
                    f.write(json.dumps(fileContent,indent=4))


