from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.schema import HumanMessage,AIMessage,SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

#Fewshot Learning
# - 모델에게 생성하는 대답의 예제를 전달
# - 기본적인 messages(system)을 활용한 엔지니어링보다 훨씬 더 강력한 성능을 보임
# - 즉, prompt 작성보다 예제를 보여주는 fewshot이 훨씬 더 좋음
# - 대화기록 등 DB에서 가져와서 fewshot 사용 


#fewshot 예제
examples = [
    {
        "question": "What do you know about France?",
        "answer": """        
        Here is what I know:        
        Capital: Paris        
        Language: French        
        Food: Wine and Cheese        
        Currency: Euro       
        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """        
        I know this:        
        Capital: Rome        
        Language: Italian        
        Food: Pizza and Pasta        
        Currency: Euro        
        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """        
        I know this:        
        Capital: Athens        
        Language: Greek        
        Food: Souvlaki and Feta Cheese        
        Currency: Euro        
        """,
    },
]



_ = load_dotenv(find_dotenv())


# 1.chat 모델 생성
chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    # 답변 생성하는 과정을 시각화 가능
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

example_prompt = PromptTemplate.from_template(
    "Human: {question}\nAI:{answer}"
)

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)

chain = prompt | chat
chain.invoke({
    "country" : "Japan"
})