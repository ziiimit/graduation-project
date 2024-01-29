from langchain_community.document_loaders import YoutubeLoader
import os



def getArticleSetTransctipt(theme,url,title):

    # 获取articleSet的transcript
    path = f"/Users/huangshihui/Downloads/backend/data/raw_transcript/{theme}/{title}.txt"

    # 加载transcript
    loader = YoutubeLoader.from_youtube_url(
        url, add_articleSet_info=False
        # language=['en-US']
    )

    # 写入文件
    with open(path,"a",encoding="utf-8") as f:
        result = loader.load()
        for item in result:
            f.write(item.page_content)

    # 在generated_article对应目录下，构建存放generated article的目录
    article_dir_path = f"/Users/huangshihui/Downloads/backend/data/generated_article/{theme}/{title}"
    os.mkdir(article_dir_path)







