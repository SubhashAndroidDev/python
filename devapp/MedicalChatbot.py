import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(page_title="Medical Chatbot", page_icon="🏥")

st.title("🏥 AI Medical Assistant")
st.caption("⚠️ This chatbot provides general health information only. Not a doctor.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 🧠 SYSTEM PROMPT (VERY IMPORTANT)
SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are a strict medical assistant AI.

RULES (VERY IMPORTANT):
1. ONLY answer medical or health-related questions.
2. If the question is NOT related to health, reply EXACTLY with:
   "❌ This assistant is only for medical-related questions."
3. Do NOT answer general knowledge (fruits, politics, coding, etc.)
4. Do NOT generate images or unrelated content.
5. Do NOT provide medical diagnosis or prescriptions.
6. Provide only general health information.
7. For emergency symptoms (chest pain, breathing issues, unconsciousness), say:
   "🚨 This may be a medical emergency. Seek immediate medical help."

Be strict. Do not break these rules under any condition.
"""
}

# Show previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Describe your symptoms or ask health question...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)

    # Save user message
    st.session_state["messages"].append({
        "role": "user",
        "content": user_input
    })

    # Prepare conversation
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