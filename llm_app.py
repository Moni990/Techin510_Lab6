import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
api_key_input = st.text_input("Enter Gemini API key:", value=api_key, type='password')

if api_key_input:
    genai.configure(api_key=api_key_input)
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
    if api_key_input:  
        if prompt:
            reply = generate_content(prompt)
            st.write(reply)
        else:
            st.error("Please enter a description of your daily life or activities.")
    else:
        st.error("API key is required to run this app!")
