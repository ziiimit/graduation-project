# 确保相对路径在不同的主机上都有效
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)
from utils.path import *
from utils.dataDirReadandWrite import writeTranscript

import time

# https://github.com/jdepoix/youtube-transcript-api/
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound
# 爬虫工具，文档：https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# 将 "时:分:秒" 转化为秒
def transformTimeFormat(originalTimeStr):
    components = originalTimeStr.split(":")
    res = 0
    if len(components)==2:
        res += int(components[0]) * 60 
        res += int(components[1])
    else:
        res += int(components[0]) * 60 * 60
        res += int(components[1]) * 60 
        res += int(components[2]) 
    return res
            
# 爬取视频标题、视频描述中的timestamps字符串
# 确保机子能上外网且网不要太慢 & 有Firefox浏览器
# 网慢就将下面sleep时间增加，没有firefox就改用别的浏览器
def spider(url):
    driver = webdriver.Firefox()
    driver.get(url)

    # 接下来都是一些浏览器界面操作，必须这样操作页面才会有想要的内容。。。。
    # 点击接受Cookie
    time.sleep(5)  # 等待对话框加载，不然找不到element报错
    try:
        button_acceptCookie = driver.find_element(By.CSS_SELECTOR,'.eom-buttons .eom-button-row:nth-child(1) ytd-button-renderer:nth-child(2) button')
        button_acceptCookie.click()
    except NoSuchElementException:
        print('没有弹出cookie确认框')
  
    # 获取视频title
    title = driver.find_element(By.XPATH, "//div[@id='above-the-fold']/div[@id='title']/h1").text.strip()
    
    # 点击more，查看descriptino详情
    time.sleep(10)
    button_descriptionMore = driver.find_element(By.CSS_SELECTOR,'ytd-text-inline-expander tp-yt-paper-button#expand')
    button_descriptionMore.click()

    descriptionSpanList = driver.find_elements(By.CSS_SELECTOR, "#description #description-inner ytd-text-inline-expander yt-attributed-string span span")
    timestamps = []
    for i in range(len(descriptionSpanList)):
        if(descriptionSpanList[i].text.startswith("Timestamps")):
            timestampsElementIndex = i+1
            while(descriptionSpanList[timestampsElementIndex].text[0].isdigit()):
                timestampsElement = {
                    'startTime': transformTimeFormat(descriptionSpanList[timestampsElementIndex].text),
                    'segmentTitle':descriptionSpanList[timestampsElementIndex + 1].text.split('\n')[0].strip()
                }
                timestampsElementIndex += 2
                timestamps.append(timestampsElement)

    driver.close()
    
    return {
        'videoTitle':title,
        'timestamps': timestamps
    }


# 获得根据timestamps切割的transcript segment list
def getTranscriptSegments(videoID,timestamps,abandonList):

    try:
        transcripts = YouTubeTranscriptApi.get_transcript(videoID)
    except NoTranscriptFound:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id=videoID).find_manually_created_transcript(['en-US']).fetch()

    # YouTubeTranscriptsApi返回的数据格式为[{'text': "..", 'start': 402.67, 'duration': 3.87}]，这里的start和timestamps里的时间不一致，无法直接通过timestamps来划分segment
    # 解决方案：
        # 遍历返回值, 将start值与timestamps中的startTime相差不大于tolerance(秒)的句子设置为断点，并将对应index存储至breakpoints列表中
    # 思路:
        # youtubeTranscriptsAPI的句子切割时间点与原视频的timestamps的时间点之间不是完全相等的，一方面是前者精确到了0.01秒，另一方面是原视频的timestamps并不总是在一个句子刚开始时切割的
        # 因此，原视频timestamps的时间点所指的那个句子在api中对应的时间值，可能与timestamps的时间值有一定的距离，这里假设为tolerance
    # tolerance设置为多少秒合适：
        # tolerance的值取小了，可能导致断点丢失；取大了，可能存在位置连续的断点，即冗余的断点；
        # 假设tolerance值取得比较好，不存在丢失的断点，breakpoints内的元素与原视频timestamps的元素之间的映射关系为多对一的满射
    tolerance = 10
    breakpoints = []
    for i in range(len(transcripts)):

        start_trans = transcripts[i]['start']

        for item in timestamps:
            start_stamps = item['startTime']
            if abs( start_trans - start_stamps ) <= tolerance:
                breakpoints.append(i)

    print("breakpoints start value:")
    print([transcripts[index]['start'] for index in breakpoints])

    # 接下来就是将breakpoints中连续的冗余断点清除
    # 如果断点之间相差的值<=tolerance * 2, 说明其所指向的是timestamps中的同一个断点
    distance = tolerance * 2
    currentIndex = 0
    while True:

        # 越界检查
        if( not currentIndex < len(breakpoints) - 1 ):
            break

        if(transcripts[breakpoints[currentIndex + 1]]['start'] - transcripts[breakpoints[currentIndex]]['start'] <= distance ):
            breakpoints.remove(breakpoints[currentIndex + 1])
        else: 
            currentIndex += 1
    print("breakpoints  start value after clearing:")
    print([transcripts[index]['start'] for index in breakpoints])


    assert len(breakpoints) == len(timestamps)

    # 获取transcripts按照timestamps标题划分的segments列表
    segments = []
    for i in range(len(breakpoints)):

        # 去除和视频主题无关的赞助内容等
        # 获取当前timestamps中的
        segmentTitle = timestamps[i]['segmentTitle'] 
        shouldAbandon = False
        for item in abandonList:
            if item.lower() in segmentTitle.lower():
                shouldAbandon = True
                print('abandon: ',segmentTitle)
                break
        if shouldAbandon:
            continue

        # 拼接segment
        text = ""
        start = breakpoints[i]
        if i == len(breakpoints) - 1: 
            sentences = transcripts[start:]
            for s in sentences:
                text += s['text'] + " "
        else:
            end = breakpoints[i+1]
            sentences = transcripts[start:end]
            for s in sentences:
                text += s['text'] + " "
      

        segment = {
            "text":text,
            "segmentTitle": segmentTitle.strip()
        }
        segments.append(segment)
    
    return segments


 
def main(videoURL,theme,abandonList):

    print("start getting transcript")

    ###############
    print("spider, getVideoInfo")
    videoInfo = spider(videoURL)
    videoTitle = videoInfo['videoTitle'].split('|')[0].strip()
    timestamps = videoInfo['timestamps']
    print("spider result:")
    print("video title:",videoTitle)
    print("timestamps without title:")
    print([item['startTime'] for item in timestamps])
    ################
    print("get segements")
    videoID = videoURL.split('=')[-1]
    segments = getTranscriptSegments(videoID=videoID,timestamps=timestamps,abandonList=abandonList)
    ################
    print("write file")
    fileContent = {
        'meta':{
            'videoURL':videoURL,
            'videoTitle':videoTitle,
            'theme':theme
        },
        'transcriptSegments':segments
    }
    writeTranscript(theme=theme,videoTitle=videoTitle,fileContent=fileContent)
    print("done writing")
    #################
    return videoTitle



            



