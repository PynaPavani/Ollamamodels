import streamlit as st
import os
from langchain_community.llms import Ollama


st.title('Ollama Models chatbot')


option = st.selectbox(
   'Select Ollama model',
   ("gemma:2b", "mistral", "llama3","llama2",'phi3'),
   index=None,
   placeholder="Select ollama model...",
)
if option is not None:
    st.write("The model selected is :", option)

query= st.text_input('enter Your Query')

if query:
    llm = Ollama(temperature=0,model=option)
    response=llm.invoke(query)
    st.write(response)


