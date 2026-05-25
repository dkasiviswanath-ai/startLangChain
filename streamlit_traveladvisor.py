
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
#from langchain_core.globals import set_debug

#set_debug(True)
load_dotenv()

prompt_template = PromptTemplate(
input_variables = ["country"],
template =""" You are an expert in traditional cuisines. You provide specific dish from a country. Answer the question: What is the traditional cusine of {country}?"""
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY, temperature=0.9)
st.title("Cuisine Info")

country = st.text_input("Enter your country?")
response = llm.invoke(prompt_template.format(country=country))

if country:
    st.write(response.content)
