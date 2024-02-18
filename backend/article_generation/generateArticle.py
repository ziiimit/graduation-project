from langchain.prompts import PromptTemplate
from openai import OpenAI


api_key = "sk-zk29795f32167f6443e112ce116990fe14f65d1947169cd3"
base_url = "https://flag.smarttrot.com/v1/"


# 首先，移除transcripts中和主体无关的内容，如寒暄、自我介绍、品牌推广等内容
# 以视频的标题作为中心主题，去除无关的内容
def filter(rawText,title):
    client = OpenAI(api_key=api_key,base_url=base_url)

    template=f"""
        Subject: {title}
        Text:{rawText}
    """
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role":"system", "content":"Your job is to filter the content of the given text that is irrelevant to the given subject"},
            {"role":"system", "content":"Response should only contain filtered text with no blankline."},
            {"role":"user", "content":template}
        ]
    )
    
    print(resp.choices[0].message.content)


def generateArticleRawText(rawText, theme, articleSetCaption, articleIndex):
   
   prompt = PromptTemplate(
      template="""
        Write an article based on the given video transcripts

        Content should only include plain paragraphs and no subtitle.
        Content should be easy to read and understood.

        Filter the content that is irrelevant to the subject "ADHD & How Anyone Can Improve Their Focus"

        Output Format: first line is title , next line follows the article content body.

        Separate the article into paragraphs.

        Text：{rawText}""",
        input_variables=["rawText"],
    )
   
   chain = prompt | MODEL 

   output = chain.invoke({"rawText": rawText})

   prefix = "/Users/huangshihui/Downloads/backend/data/generated_article/"
   path = prefix + theme +"/" + articleSetCaption + "/" + f"{articleIndex}.txt"

   with open(path,"a") as f:
      f.write(output.content)



def getArticleRawText(theme, articleSetCaption, articleIndex):
    prefix = "/Users/huangshihui/Downloads/backend/data/generated_article/"
    path = prefix + theme +"/" + articleSetCaption + "/" + f"{articleIndex}.txt"
    with open(rf'{path}') as f:
        return f.read()
    


def getArticleObject(rawText, articleIndex):
    parts = rawText.split('\n\n')
    title = parts[0].capitalize()
    paragraphList = parts[1:]
    return {
        "title": title,
        "paragraphList":paragraphList,
        "sequence":articleIndex
    }


# with open(r'/Users/huangshihui/Downloads/graduation-project/backend/data/generated_article/mental_health_and_addiction/The Scienc & Treatment of Bipolar Disorder/0.txt')  as f:
#     print(f.read())

# print(getArticleRawText('mental_health_and_addiction','The Scienc & Treatment of Bipolar Disorder',0))
    

   


