# OPENAI API 사용하기
# platform.openai.com
# 1.API - key 발급
# 2. 카드 등록(VISA, MASTER) + 5.5달러(보유)


# 라이브러리 관리
# 1.VENV (가상환경)
# 2.Anaconda

# python -m venv ./venv
# .\venv\Scripts\activate
# pip install

from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "모든 설명을 3줄로 요약해서 설명해주세요"},
    {"role": "user", "content": "클라우드 설명해줘"}
  ]
)

print(completion.choices[0].message)


# OpenAI의 API를 사용해서 챗봇 문제점 
# 1. 개발이 어려움(난이도 상) -> 더 쉽게 개발 할 수 있는 무언가가 필요 -> 프레임워크
# 2. 챗봇 개발 완성 -> Bard 모델 변경 -> Bard API로 처음부터 개발 -> 프레임워크(LLM)

# -> LangChain프레임워크를 쓰면 코드는 동일한데 모델만 바꾸면 API가 바껴서 실행 
