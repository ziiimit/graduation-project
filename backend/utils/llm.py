from openai import OpenAI

# chat接口要钱，记错openAI账号注册时间，赠送的5刀用了一点点就过期了，充值要国外银行卡
# https://github.com/xing61/xiaoyi-robot?tab=readme-ov-file 可以用支付宝充值，比原价多了一点点，接口调用形式和openAI是一样的
api_key = "sk-zk29795f32167f6443e112ce116990fe14f65d1947169cd3"
base_url = "https://flag.smarttrot.com/v1/"
client = OpenAI(api_key=api_key,base_url=base_url)  # https://docs.zhizengzeng.com/ru-men/jie-kou-shi-li/mo-xing-tiao-yong-shi-li



def chat(messages,model="gpt-3.5-turbo-0125"):
    
    resp = client.chat.completions.create(
        model=model, 
        messages=messages
    )

    return resp.choices[0].message.content