import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_groq import ChatGroq

google_api_key = st.secrets.GOOGLE_API_KEY
groq_api_key = st.secrets.GROQ_API_KEY


def gemini_enhancer(pmt):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
    prompt = f"""
    Your task is to enhance the following prompt to make it more detailed, engaging, and effective for large language model interactions. Consider clarity, specificity, and relevance to the topic. Add any necessary context or examples to improve the prompt. dont give any extra info directly give the output. refined prompt should be short and to the point.

    Original prompt:
    "{pmt}"

    """

    result = llm.invoke(prompt)
    return result.content

# print(gemini_enhancer("heyy"))

def groq_enhancer(pmt):
    llm = ChatGroq( model="llama-3.1-8b-instant", api_key=groq_api_key )
    prompt = f"""
    Your task is to enhance the following prompt to make it more detailed, engaging, and effective for large language model interactions. Consider clarity, specificity, and relevance to the topic. Add any necessary context or examples to improve the prompt. dont give any extra info directly give the output. refined prompt should be short and to the point.

    Original prompt:
    "{pmt}"

    """
    result = llm.invoke(prompt)
    return result.content


# print(groq_enhancer("i wanna make readme file for house price prediction"))