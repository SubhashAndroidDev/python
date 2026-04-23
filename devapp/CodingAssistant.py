import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(page_title="AI Coding Agent", page_icon="💻")

st.title("💻 AI Coding Assistant (Coding Only)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ SYSTEM MESSAGE (VERY IMPORTANT)
SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are an AI Coding Assistant.

Rules:
1. Only answer programming/coding related questions.
2. If the user asks anything non-coding (e.g. weather, jokes, general knowledge),
   reply strictly with:
   "❌ This assistant is only for coding-related questions."
3. Provide clean, correct, and beginner-friendly code.
4. Explain code step-by-step when needed.
5. Support Python, JavaScript, Java, C++, SQL, etc.
"""
}

# Show previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask coding question...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)

    # Save user message
    st.session_state["messages"].append({
        "role": "user",
        "content": user_input
    })

    # Prepare full conversation
    full_messages = [SYSTEM_PROMPT] + st.session_state["messages"]

    # Get AI response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=full_messages
        )

        ai_reply = response.choices[0].message.content
        st.markdown(ai_reply)

    # Save AI response
    st.session_state["messages"].append({
        "role": "assistant",
        "content": ai_reply
    })