# import streamlit as st


# st.title("Streamlit 웹 애플리케이션 with Elice")

# st.header('1. 정적 페이지 만들기')

# st.markdown("""
#             정적 페이지를 만드는 데에도 많은 요소가 활용될 수 있습니다.
#             """)

# st.code("""
#         예를 들어 코드블럭은 코드를 쓰기도 좋지만, 글자를 강조하고 싶을때 사용해도 유효합니다.
#         """)


# st.caption("caption 기능은 인용구나, 각주등을 넣을 때 사용하기 좋습니다.")


# name = st.text_input("text_input의 기능을 사용하여, 사람의 이름, 연락처 등 각종 사용자 입력을 받아볼 수 있습니다.",placeholder="홍길동")


# if st.button('입력'):
#     st.write(f'{name}님, 환영합니다.')

# # input widget 실습
# uploaded_file = st.file_uploader("Choose a csv file")
# if uploaded_file:
#     st.write("파일 이름: ",uploaded_file.name)
    
# # 선택박스 widget
# option = st.selectbox(
# 'How would you like to be contacted?',
# ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)



# with st.sidebar:
#     add_selectbox = st.selectbox(
#         "How would you like to be contacted? ",
#         ("Email", "Home phone", "Mobile phone")
#     )   
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

# st.write(add_radio)

import openai
import streamlit as st

# OpenAI API 키 설정
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Streamlit 앱 설정
st.set_page_config(page_title="ChatGPT 챗봇", page_icon="🤖")

st.title("🤖 ChatGPT 챗봇")
st.write("💬 OpenAI GPT 기반 챗봇입니다. 질문을 입력하세요!")

# 세션 상태 초기화 (채팅 내역 저장)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 채팅 내역 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
user_input = st.chat_input("질문을 입력하세요...")

if user_input:
    # 사용자 메시지 저장 및 표시
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # OpenAI API 호출
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
        api_key=OPENAI_API_KEY
    )

    bot_reply = response["choices"][0]["message"]["content"]

    # 챗봇 응답 저장 및 표시
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
