from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from article_generation.getTranscripts import article_dir_path, transcript_path
import os



openai_api_key = "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"
MODEL = OpenAI(openai_api_key=openai_api_key, temperature=0)




def generateArticleRawText(rawText, theme, articleSetCaption, articleIndex):
   
   prompt = PromptTemplate(
      template="""
        You are the author of the text below, write an article based on it,
        pay attention to the knowledge with regard to the neuroscience and the advice if is given.
        
        Title should be as simple as possible

        Content must not have conclusion.
        Content should only include plain paragraph and no subtitle.
        Content should be easy to read and understood.

        Output Format: first line is title , next line follows the article content body.

        Separate the article into paragraphs.

        Text：{text}""",
        input_variables=["text"],
    )
   
   chain = prompt | MODEL 

   output = chain.invoke({"text": rawText})

   prefix = "/Users/huangshihui/Downloads/backend/data/generated_article/"
   path = prefix + theme +"/" + articleSetCaption + "/" + f"{articleIndex}.txt"

   with open(path,"a") as f:
      f.write(output.content)




def getArticleRawText(theme, articleSetCaption, articleIndex):
    prefix = "/Users/huangshihui/Downloads/backend/data/generated_article/"
    path = prefix + theme +"/" + articleSetCaption + "/" + f"{articleIndex}.txt"
    with open(path) as f:
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




    


   


