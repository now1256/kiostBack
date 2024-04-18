from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# from LLM_SDK.Runnable_memory import chain_memory
from LLM_SDK.fewshot_prompt import main_prompt, order_prompt, menu_prompt

import json
from fastapi import APIRouter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import chain

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
os.environ["OPENAI_API_KEY"] = "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"

router = APIRouter(prefix="/status")

main_chain = main_prompt() | ChatOpenAI(temperature=0)| StrOutputParser()

menu_chain = (
    menu_prompt()
    # OpenAI의 LLM을 사용합니다.
    | ChatOpenAI(temperature=0)
)

order_chain = (
    order_prompt()
    # OpenAI의 LLM을 사용합니다.
    | ChatOpenAI(temperature=0)

)
vectorstore = FAISS.from_texts(
    ["커피숍 assistant로 질문을 받는 assistant이다."
     "인사를 하면 친절하게 대답한다"
     "화장실은 문열고 나가서 옆건물 1층에 있습니다"
     "기본적인 커피 옵션은 얼음,시럽,온도로 얼음은 적게 중간 많이가 있고 시럽은 넣고, 안넣고가 있으며 온도는 뜨거움과 차가움이 있습니다."
     "모카라떼의 경우 기본커피옵션에 휘핑크림 넣기 안넣기가 있습니다."]
    , embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
template = """Answer the question based on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

general_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | ChatOpenAI(temperature=0)
)




# chain과 memory 결합
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}  # 세션 기록을 저장할 딕셔너리


# 세션 ID를 기반으로 세션 기록을 가져오는 함수
def get_session_history(session_ids: str) -> BaseChatMessageHistory:
    print(session_ids)
    if session_ids not in store:  # 세션 ID가 store에 없는 경우
        # 새로운 ChatMessageHistory 객체를 생성하여 store에 저장
        store[session_ids] = ChatMessageHistory()
    return store[session_ids]  # 해당 세션 ID에 대한 세션 기록 반환


@chain
def custom_chain(text):
    # 첫 번째 프롬프트, ChatOpenAI, 문자열 출력 파서를 연결하여 체인을 생성합니다.
    output = main_chain.invoke({"input": text})
    print(output)  # AIMessage 객체의 내용을 확인합니다.

    # 첫 번째 결과가 "order"인 경우에만 두 번째 체인 실행
    if output == "order":
        with_message_history = RunnableWithMessageHistory(
            order_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return with_message_history.invoke({"input": text}, config={"configurable": {"session_id": "123"}})

    elif output == "menu":
        with_message_history = RunnableWithMessageHistory(
            menu_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return with_message_history.invoke({"input": text}, config={"configurable": {"session_id": "123"}})

    # "order"나 "menu"가 아닌 다른 결과인 경우 그대로 반환합니다.
    return general_chain.invoke(text)


@router.post("")
def process_input(input_data):
    output = custom_chain.invoke(input_data).content
    try:
        output = json.loads(output)
    except json.JSONDecodeError:
        # 입력 데이터가 JSON 형 식이 아닌 경우 그대로 사용
        output = {"output": output}
    return output


