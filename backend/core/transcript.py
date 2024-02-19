# 确保相对路径在不同的主机上都有效
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

import json
import time

# https://github.com/jdepoix/youtube-transcript-api/
from youtube_transcript_api import YouTubeTranscriptApi

# 爬虫工具，文档：https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
from selenium import webdriver
from selenium.webdriver.common.by import By


# 将 "时:分:秒" 转化为秒
def transformTimeFormat(originalTimeStr):
    components = originalTimeStr.split(":")
    res = 0
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
    button_acceptCookie = driver.find_element(By.CSS_SELECTOR,'.eom-buttons .eom-button-row:nth-child(1) ytd-button-renderer:nth-child(2) button')
    button_acceptCookie.click()
  
    # 获取视频title
    title = driver.find_element(By.XPATH, "//div[@id='above-the-fold']/div[@id='title']/h1").text.strip()
    
    # 点击more，查看descriptino详情
    time.sleep(10)
    button_descriptionMore = driver.find_element(By.CSS_SELECTOR,'ytd-text-inline-expander tp-yt-paper-button#expand')
    button_descriptionMore.click()

    descriptionSpanList = driver.find_elements(By.CSS_SELECTOR, "#description #description-inner ytd-text-inline-expander yt-attributed-string span span")
    timestamps = []
    for i in range(len(descriptionSpanList)):
        if(descriptionSpanList[i].text == "Timestamps"):
            timestampsElementIndex = i+1
            while(descriptionSpanList[timestampsElementIndex].text.startswith('0')):
                timestampsElement = {
                    'startTime': transformTimeFormat(descriptionSpanList[timestampsElementIndex].text),
                    'segmentTitle':descriptionSpanList[timestampsElementIndex + 1].text
                }
                timestampsElementIndex += 2
                timestamps.append(timestampsElement)

    driver.close()
    
    return {
        'videoTitle':title,
        'timestamps': timestamps
    }


# YouTubeTranscriptsApi返回的数据格式为[{'text': "..", 'start': 402.67, 'duration': 3.87}]
# 根据timestamps将句子进行拼接
# 返回[{"text":,"segmentTitle":}]
def getTranscriptSegments(videoID,timestamps):
    transcripts = YouTubeTranscriptApi.get_transcript(videoID)

    # 遍历transcripts, 将start值与timestamps中的startTime相差不大于tolerance(秒)的句子设置为断点， 将该句子的index存储至breakpoints列表中
    # youtubeTranscriptsAPI的句子切割时间点与原视频的timestamps的时间点之间不是完全相等的，一方面是前者精确到了0.01秒，另一方面是原视频的timestamps并不总是在一个句子刚开始时切割的
    # 因此，原视频timestamps的时间点所指的那个句子在api中对应的时间值，可能与timestamps的时间值有一定的距离，这里假设为tolerance
    # tolerance的值取小了，可能导致断点丢失；取大了，可能存在位置连续的断点，即冗余的断点；
    tolerance = 2
    breakpoints = []
    for i in range(len(transcripts)):

        start = transcripts[i]['start']

        for item in timestamps:
            startTime = item['startTime']
            if abs(start-startTime) <= tolerance:
                breakpoints.append(i)


    # 假设tolerance值取得够大，不存在丢失的断点，breakpoints内的元素与原视频timestamps的元素之间的映射关系为多对一的满射
    # 接下来就是将位置连续的冗余断点清除
    # 假设（不保证一定能清干净，但估计是没问题）最多会同时出现distance + 1 个位置连续的断点，清除连续体后面distance个
    # 为了确保冗余断点彻底清除，distance可以设置得大一点，毕竟原视频的timestamps之间肯定间隔了很多句话，不用担心清掉了不改清的断点
    # 但是不能大到吞掉了真正的下一个断点
    distance = 8
    currentItemIndex = 0
    while True:
        if( not currentItemIndex < len(breakpoints) - 1 ):
            break
        if(breakpoints[currentItemIndex + 1]-breakpoints[currentItemIndex] <= distance ):
            breakpoints.remove(breakpoints[currentItemIndex + 1])
        else: 
            currentItemIndex += 1

    # 检查原视频的timestamps和我们找到的breakpoints的断点数量是否一样
    assert len(timestamps) == len(breakpoints)
    
    # 获取transcripts按照timestamps标题划分的segments列表
    segments = []
    for i in range(len(breakpoints)):
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
      

    
        # 去除和视频主题无关的赞助内容
        segmentTitle = timestamps[i]['segmentTitle']
        if ('sponsor' in segmentTitle) or ('Sponsor' in segmentTitle) or ('sponsors' in segmentTitle) or ('Sponsors' in segmentTitle):
            print('abandon: ',segmentTitle)
            continue

        segment = {
            "text":text,
            "segmentTitle": segmentTitle
        }
        segments.append(segment)
    
    return segments


 
def main():

    videoURL = "https://www.youtube.com/watch?v=zVCaYyUWWSw"
    theme = 'focus_productivity_and_creativity'

    video_info = spider(videoURL)
    videoTitle = video_info['videoTitle']
    timestamps = video_info['timestamps']

    videoID = videoURL.split('=')[-1]
    segments = getTranscriptSegments(videoID=videoID,timestamps=timestamps)

    # 存储到文件中
    fileContent = {
        'metadata':{
            'videoURL':videoURL,
            'videoTitle':videoTitle,
            'theme':theme
        },
        'transcriptSegments':segments
    }
    path = PROJECT_ROOT + f'/data/raw_transcript/{theme}/{videoTitle}.json'
    with open(path,"w",encoding="utf-8") as f:
        f.write(json.dumps(fileContent,indent=4))


main()
            



