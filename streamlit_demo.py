import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
#from langchain_core.globals import set_debug

#set_debug(True)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY, temperature=0.9)
st.title("OpenAI with Streamlit")

question = st.text_input("What is your question? ")
response = llm.invoke(question)

if question:
    response = llm.invoke(question)
    st.write(response)
