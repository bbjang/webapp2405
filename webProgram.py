# 설치 필요
# pip install langchain
import openai
import streamlit as st
from langchain_community.llms import OpenAI


st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))


# with st.form('my_form'):
#  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
#  submitted = st.form_submit_button('Submit')
#  if not openai_api_key.startswith('sk-'):
#    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
#  if submitted and openai_api_key.startswith('sk-'):
    
#    generate_response(text)




# 텍스트 파일 업로드
uploaded_file = st.file_uploader("텍스트 파일을 업로드하세요.", type=["txt"])

# 질문 입력
question = st.text_input("질문을 입력하세요.")

# 텍스트 파일에서 질문에 대한 답변 검색
if uploaded_file is not None and question:
    # 텍스트 파일 처리 및 텍스트 추출
    text = uploaded_file.getvalue().decode("utf-8")
    
    # OpenAI API를 사용하여 답변 검색
    answer = search_answer(question, text)
    
    # 결과 출력
    if answer:
        st.success("답변: {}".format(answer))
    else:
        st.error("답변을 찾을 수 없습니다.")
