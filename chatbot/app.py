from langchain_openAI import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt

prompt=ChatPromptTemplate.from_messages(
    [
       ('system','You are a helpful assistant. Please respond to the user queries'),
       ('user','Question:{question}')
    ]
)

## streamlit framework

st.title("Langchain Demo with OpenAI API")
input_text=st.text_input("Search the topic u want")

## OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output=StrOutputParser()

chain=prompt|llm|output

if input_text:
    st.write(chain.invoke({'question':input_text}))