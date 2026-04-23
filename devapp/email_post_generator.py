import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load env
load_dotenv()
client=OpenAI(api_key=os.getenv("OPEN_API_KEY"))

st.set_page_config(page_title="AI Content Generator")

st.title(" AI Email $ LinedIn Post Generator")


#Input fields
topic=st.text_input("Enter Topic")
tone=st.selectbox("Select Tone",["Professional","Casual","Friendly"])

content_type=st.radio("Select Content Type",["Email","LinkedIn Post"])

#Generate function
def generate_content(topic,tone,content_type):
    if content_type == "Email":
        prompt=f"Write a professinal email about {topic} in a {tone}, tone."
    else:
        prompt=f"Write a LinkedIn post about {topic} wth hashtags in a {tone} tone."

    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content":"You are a helpful content writer."},
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )   

    return response.choices[0].message.content


#button
if st.button("Generate"):
    if topic:
        output=generate_content(topic,tone,content_type)
        st.write(output)
    else:
        st.warning("Please enter a topic")    