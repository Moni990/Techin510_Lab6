import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are very skilled at writing Vlog scripts. 

Please write a complete and colorful video script based on the general content provided by the user.

Please include the following details:
- Introduction:
- Content:
  segments; details; visuals and interactions
- Conclusions


The user's request is:
{prompt}
"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("🏝️ Vlog Director")

prompt = st.text_area("Enter your daily life or activities:")
if st.button("Give me a Vlog script!"):
    print(prompt)
    reply = generate_content(prompt)
    st.write(reply)