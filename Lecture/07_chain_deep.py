from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain.schema import HumanMessage,AIMessage,SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutOutCallbackHandler

_ = load_dotenv(find_dotenv())


# 1.chat 모델 생성
chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    # 답변 생성하는 과정을 시각화 가능
    streaming=True,
    callbacks=[StreamingStdOutOutCallbackHandler()]
)