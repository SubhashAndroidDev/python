import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# 🔹 Page config
st.set_page_config(page_title="AI Chat", layout="wide")

st.title("💬 AI Chat Assistant")

# 🔹 Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
        api_key=api_key

)

# 🔹 Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔹 Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{input}")
])

# 🔹 Chain
chain = prompt | llm

# 🔹 Trim function (token control)
def trim_history():
    MAX_MESSAGES = 10
    if len(st.session_state.chat_history) > MAX_MESSAGES:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_MESSAGES:]


# 🔹 Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# 🔹 Input box (ChatGPT style)
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    response = chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)

    # Save to memory
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=response.content))

    # Trim history
    trim_history()