# 确保相对路径在不同的主机上都有效
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


def writeFile(path,content):
    path = PROJECT_ROOT + path

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)


           

