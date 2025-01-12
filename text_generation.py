import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

genai_api_key = st.secrets["genai"]["api_key"]
genai_api_key = st.secrets["genai"]["api_key"]

# Use the API keys as needed

load_dotenv()  # Loading env
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
GENAI_API_KEY = st.secrets["genai"]["api_key"]


def initialize_text_model():
    genai.configure(api_key=GENAI_API_KEY)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    return genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )


def generate_text(query, chat_session):
    response = chat_session.send_message(query)
    return response.text


def text_generation_app(chat_session):
    st.title("Text Generation")

    with st.sidebar:
        st.header("Your search History")

        # Initial history at 0
        if "history" not in st.session_state:
            st.session_state.history = []

        # Initial + 1 history then:
        if st.session_state.history:
            for i, query in enumerate(reversed(st.session_state.history)):
                st.write(f"{len(st.session_state.history) - i}. {query}")

    user_input_text = st.text_area("Shoot your query:")
    if st.button("Generate Now!"):
        if user_input_text.strip():
            response = generate_text(user_input_text, chat_session)

            st.session_state.history.append(user_input_text)

            st.markdown(f"**My Answer:** {response}")
        else:
            st.error("Please enter something!")
