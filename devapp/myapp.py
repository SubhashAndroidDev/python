import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv("D:/python/gen_ai_april/.env")

llm = ChatOpenAI(model="gpt-4o-mini")

#model.generate("What is the capital of France?")
response = llm.invoke("What is the capital of India?")
print(response.response_metadata)
st.title("CHAT With Subhash")
st.write("This is a Streamlit app using the gen-ai-foundation package.")


user_input = st.text_input("Ask a question:", key="user_input")
if st.button("Submit" ):
    if user_input:
        response = llm.invoke(user_input)
        st.write("Response:", response.text)
    else:
        st.write("Please enter a question.")