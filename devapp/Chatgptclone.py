import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(page_title="AI ChatGPT Clone", page_icon="🤖")

st.title("🤖 AI ChatGPT Clone (GPT-4o-mini)")

# ✅ Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ Display previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ✅ Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)

    # ✅ Save user message (FIXED)
    st.session_state["messages"].append({
        "role": "user",
        "content": user_input
    })

    # ✅ Get AI response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )

        ai_reply = response.choices[0].message.content
        st.markdown(ai_reply)

    # ✅ Save AI response
    st.session_state["messages"].append({
        "role": "assistant",
        "content": ai_reply
    })