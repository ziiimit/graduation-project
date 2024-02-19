import json
from openai import OpenAI
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# chat接口要钱，记错openAI账号注册时间，赠送的5刀用了一点点就过期了，充值要国外银行卡
# https://github.com/xing61/xiaoyi-robot?tab=readme-ov-file 可以用支付宝充值，比原价多了一点点，接口调用形式和openAI是一样的
api_key = "sk-zk29795f32167f6443e112ce116990fe14f65d1947169cd3"
base_url = "https://flag.smarttrot.com/v1/"
client = OpenAI(api_key=api_key,base_url=base_url)  # https://docs.zhizengzeng.com/ru-men/jie-kou-shi-li/mo-xing-tiao-yong-shi-li



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


# filterIrrelevantContent(segmentTitle="Oral Health",text="""
#     "welcome to the huberman Lab podcast where we discuss science and science-based tools for everyday [Music] life I'm Andrew huberman and I'm a professor of neurobiology and Opthalmology at Stanford school of medicine today we are discussing oral health now when most people hear oral health they immediately think tooth health and appearance and presumably fresh breath or lack of bad breath as well and while of course two and breath freshness whiteness and health is a critical component of oral health today you will learn that oral health including the oral microbiome the health of your pallet your tonsils indeed the entire oral cavity is an extremely important component of General bodily health so much so that today we are going to add a seventh pillar to the so-called six pillars of mental health physical health and performance this is not a trivial step to add a seventh pillar to these six pillars if some of you have been listeners of this podcast for a while you may recall that the six pillars of mental health physical health and performance that is the six things that everyone needs to invest specific protocols into each day are in no particular order by the way sleep sunlight and light exposure generally which by extension also includes dark exposure nutrition exercise which we could also call movement both cardiovascular exercise and resistance training stress management and relationships and social engagement including relationship to self and today we are going to add oral health and microbiome health and I suppose we could generally call this oral and gut health because as you know if you think about it your mouth your oral cavity and your gut are contiguous with one another we are going to add oral and gut health as the seventh pillar of mental health physical health and performance because as you will learn today there are so many aspects of oral health and daily protocols for oral health that extend to cardiovascular health to metabolic health and indeed to brain health and to staving off diseases in all of those bodily compartments I cannot overemphasize enough how much oral health influences your general bodily health so today you will learn about Oral B biology and health we won't go tooo deep into the biology but we will go deep enough into the biology that you will learn some incredible things such as your teeth have the ability to literally fill back in cavities that have formed provided those cavities haven't gone too deep into the teeth layers yet you will learn that saliva While most people think of it as just spit is an incredible substance fluid that contains all sorts of interesting and important things that allow you to rebuild the strength of your teeth and indeed to support the health of your oral cavity and gut microbiome and body generally so saliva is super interesting and important and today you're going to learn many many protocols including zeroc cost protocols protocols that will actually save you money as well as some lowcost protocols to both restore improve and maintain oral health and in doing so maintain and improve your overall bodily Health ",
# """)

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
    # print(resp.choices[0].message.content)
    return resp.choices[0].message.content

# generateIntro(segmentTitle="Oral Health",text="""Today we are discussing oral health now when most people hear oral health they immediately think tooth health and appearance and presumably fresh breath or lack of bad breath as well and while of course two and breath freshness whiteness and health is a critical component of oral health today you will learn that oral health including the oral microbiome the health of your pallet your tonsils indeed the entire oral cavity is an extremely important component of General bodily health so much so that today we are going to add a seventh pillar to the so-called six pillars of mental health physical health and performance this is not a trivial step to add a seventh pillar to these six pillars if some of you have been listeners of this podcast for a while you may recall that the six pillars of mental health physical health and performance that is the six things that everyone needs to invest specific protocols into each day are in no particular order by the way sleep sunlight and light exposure generally which by extension also includes dark exposure nutrition exercise which we could also call movement both cardiovascular exercise and resistance training stress management and relationships and social engagement including relationship to self and today we are going to add oral health and microbiome health and I suppose we could generally call this oral and gut health because as you know if you think about it your mouth your oral cavity and your gut are contiguous with one another we are going to add oral and gut health as the seventh pillar of mental health physical health and performance because as you will learn today there are so many aspects of oral health and daily protocols for oral health that extend to cardiovascular health to metabolic health and indeed to brain health and to staving off diseases in all of those bodily compartments I cannot overemphasize enough how much oral health influences your general bodily health so today you will learn about Oral B biology and health we won't go tooo deep into the biology but we will go deep enough into the biology that you will learn some incredible things such as your teeth have the ability to literally fill back in cavities that have formed provided those cavities haven't gone too deep into the teeth layers yet you will learn that saliva While most people think of it as just spit is an incredible substance fluid that contains all sorts of interesting and important things that allow you to rebuild the strength of your teeth and indeed to support the health of your oral cavity and gut microbiome and body generally so saliva is super interesting and important and today you're going to learn many many protocols including zeroc cost protocols protocols that will actually save you money as well as some lowcost protocols to both restore improve and maintain oral health and in doing so maintain and improve your overall bodily Health.""")



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
    # print(resp.choices[0].message.content)
    list = resp.choices[0].message.content.split('\n\n')
    res = []
    for i in range(len(list)):
        res.append({
            'sequence': i,
            'text':list[i]
        })

    return 


# generateArticle(segmentTitle="Proper Teeth Brushing; Tooth Sensitivity & Gums",text="""
#     "hours some will but most won't and now of course I've been saying brushing and flossing but I haven't talked about the incredibly extensive landscape of how to brush and floss so now let's take ourselves back to being little kids right when we were taught to brush our teeth in a particular way you know you're supposed to spend a certain number of minutes set a timer supposed to floss in a certain way every time we go to the dentist they tell us to floss in a certain way do this not this what do the data really say what are the modern health professionals in dental and oral health really suggest in we do when it comes to brushing and flossing and fortunately here there's a near uniform consensus there's always that outlier that person that says to do things a little bit differently or no there's in fact one person very prominent in the dental health space that is not a fan of flossing but they are really the outlier the vast majority of dentists out there all say the same thing you need to brush you need to floss you need to do it twice a day or more and you need to do it correctly so now let's talk about what Cor correct brushing and flossing really is okay so I'm not going to demonstrate how to brush your teeth but one very actionable protocol that was told to me by all the dental professionals I spoke to was use a soft toothbrush now this one hurts or I suppose hurts less anyway it hurts my heart a little bit because I enjoy very much using a medium or hard toothbrush and really like scrubbing back there especially in the teeth in the back it just feels good I feel like I'm doing something good I get into the backs of the teeth the fronts of the teeth I know I actually enjoy brushing my teeth especially lately don't ask me why but I do but every single one of them said that that very vigorous brushing with medium or hard as they're called bristles really disrupts the interface between the teeth and the gums in ways That's not healthy for the gums and actually makes tenting of the gums and those Pockets those recesses as they're called far more likely to form and every single one of them said if you are regular with your brushing and especially if you're brushing and flossing regularly that a soft toothbrush that is one that's moved in a circular motion on the fronts and backs of your teeth for all your teeth and that is gentle you're not providing a lot of pressure is going to be the best way to break up that bofilm layer each and every time and promote the best tooth and overall oral health so I suppose um manufacturers who are making medium and hard toothbrushes maybe give us some w rationale for that um you know because the dental professionals that I spoke to and again I spoke to a fair number of them all said the same thing soft toothbrush Notch just better soft toothbrush best likewise if you use an electric toothbrush which I now do sometimes I switch back and forth but if you use an electric toothbrush it was recommended that you not provide too much pressure that you really try and keep the tips of the bristles on the the teeth and gums and yes it was also suggested that people brush their gums this is interesting for people out there who have tooth sensitivity one of the major suggestions from people in the dental and perodontal field at least the ones I spoke to was to actually brush your gums lightly to increase circulation of blood and other nutrients to the deeper portions of the tooth that actually extend into the bone now there is a tremendous amount of blood flow to the gums anyone who's um you know sort of nicked their uh gum with a while while flossing or with a toothpick can tell you bleeds very readily and that's not a good thing right you don't want to create bleeding of the gums we'll talk about bleeding of the gums during flossing in a moment by the way so don't jump the gun just yet I said jump the gun not jump the gum by the way if you are brushing your gums make sure you're using a soft toothbrush if you're using electric toothbrush make sure you're going very lightly on the gums and because there's so much blood flow to the gums it does encourage a lot of circulation to some of the deeper cavities of the tooth as it turns out I don't want to reverse to tooth anatomy in any kind of detailed way now but of course within the tooth you have again enamel you have the Dentin you've got What's called the the pulp or the center there's a lot of nerves inating the center of the tooth there's a bunch of other tissues and and the bone around it and layers Etc and when you massage or lightly brush the gums around there you're encouraging a lot of blood flow to those deeper components of the tooth which are really the live and active components of the tooth that require blood flow and nutrients so this is a good thing in fact it's probably such a good thing that most people perhaps all of us should do it but most people probably won't take the time to also brush their gums but if you have a little bit of time it can be beneficial especially if you have sensitive teeth the idea that's of emerging now in the dental field is that it can help promote resilience or less sensitivity of the teeth to things like hot and cold and ",
# """)


def main():

    theme = 'focus_productivity_and_creativity'
    videoTitle = "How to Improve Oral Health & Its Critical Role in Brain & Body Health"

    # 创建父文件夹


    # 获取transcript的segments
    path = PROJECT_ROOT + f'/data/raw_transcript/{theme}/{videoTitle}.json'
    with open(path,'r',encoding='utf-8') as f:

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
                    'title':segmentTitle,
                    'content':intro
                }
                path_intro = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}/intro.json'
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
                    'title':segmentTitle,
                    'paragraphList':generateArticle(text=text,segmentTitle=segmentTitle)
                }

                path_intro = PROJECT_ROOT + f'/data/generated_article/{theme}/{videoTitle}/article{i-1}.json'
                with open(path_intro,'w',encoding='utf-8') as f:
                    f.write(json.dumps(fileContent,indent=4))

# main()
