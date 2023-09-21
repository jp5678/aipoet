#from dotenv import load_dotenv
#load_dotenv()
import streamlit as st

#from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.predict("Hi")
#print(result)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
st.title("인공지능 시인")
content = st.text_input("주제를 입력하세요.")

if st.button("시(詩) 생성하기"):
   with st.spinner("시를 생성하고 있는 중..."):
      result = chat_model.predict(content + "이 주제의 시를 작성해줘.")
      st.write(result)

