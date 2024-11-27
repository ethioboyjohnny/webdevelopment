import streamlit as st
import requests
import json

def fetch_trivia_fact():
    response = requests.get("http://numbersapi.com/random/trivia")
    try:
        fact = response.text
    except json.JSONDecodeError:
        st.error("Error decoding the trivia fact. Please check the API response.")
        fact = "No trivia fact available at the moment."
    return fact

def interact_with_gemini(prompt, api_key):
    url = "https://gemini.googleapis.com/v1/text:generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, json=data, headers=headers)
    try:
        result = response.json()
    except json.JSONDecodeError:
        st.error("Error decoding the response from Google Gemini API. Please check the API response.")
        result = {}
    return result

st.title("Enhanced Origami Crane Tutorial with Google Gemini")
st.markdown("This page uses the Google Gemini LLM to provide additional analysis and interactive chat based on trivia facts.")

st.write("Did you know?")
trivia_fact = fetch_trivia_fact()
st.write(trivia_fact)

user_topic = st.text_input("Enter a topic related to the trivia fact for further analysis:")
user_query = st.text_input("Ask the chatbot about the trivia fact:")

gemini_api_key = "AIzaSyCAfuVEkJ_g4RqmPYYOlfjvi2WiXM8Um-Q"

if user_topic:
    gemini_prompt = f"Generate a detailed explanation about {user_topic} based on this trivia fact: {trivia_fact}"
    gemini_response = interact_with_gemini(gemini_prompt, gemini_api_key)
    st.write("Detailed Explanation:")
    st.write(gemini_response)

if user_query:
    chatbot_prompt = f"Answer this question based on the trivia fact: {trivia_fact}. Question: {user_query}"
    chatbot_response = interact_with_gemini(chatbot_prompt, gemini_api_key)
    st.write("Chatbot Response:")
    st.write(chatbot_response)
