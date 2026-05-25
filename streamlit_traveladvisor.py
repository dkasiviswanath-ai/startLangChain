
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
#from langchain_core.globals import set_debug

#set_debug(True)
load_dotenv()

prompt_template = PromptTemplate(
input_variables = ["country", "month", "language", "budget"],
template =""" You are an travel expert and provide recommendations. Consider the inputs for recommendations.
If the user provide imaginary value for country, just say I don't know.
 1. Enter the country: {country}
 2. Enter the month: {month}
 3. Enter the language: {language}
 4. Enter the budget: {budget}
 ?"""
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY, temperature=0.9)
st.title("Travel Recommendations")

country = st.text_input("Enter your country?")
month = st.text_input("Enter the month?")
language = st.text_input("Enter the language?")
budget = st.text_input("Enter your budget?")

response = llm.invoke(prompt_template.format(country=country, month=month, language=language, budget=budget))

if country:
    st.write(response.content)
