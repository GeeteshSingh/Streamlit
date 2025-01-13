import streamlit as st
import google.generativeai as genai
import os
from text_generation import text_generation_app, initialize_text_model
from image_generation import image_generation_app, initialize_image_client
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
# Initialize models
text_model = initialize_text_model()
chat_session = text_model.start_chat(history=[])
image_client = initialize_image_client()

# text generation

load_dotenv()  # Loading env
GENAI_API_KEY = os.getenv("GENAI_API_KEY")


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



# Loading env
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


def initialize_image_client():
    return InferenceClient(
        "stabilityai/stable-diffusion-3.5-large",
        token=HUGGINGFACE_API_KEY,
    )


def generate_image(description, client):
    comic_style_description = (f"{description.strip()}, in 2D comic style, cartoon-like, vibrant colors, keeping same on every new required image, and minimal "
                               f"shading")
    return client.text_to_image(comic_style_description)


def image_generation_app(client):
    st.title("Story-like Image Generation")

    # Dropdown option(Max 4)
    num_boxes = st.selectbox("Select the number of story segments (max 4):", [1, 2, 3, 4], index=0)

    # Storing descriptions in session state
    if "descriptions" not in st.session_state:
        st.session_state.descriptions = [""] * 4

    # Dynamic array boxes for story
    for i in range(num_boxes):
        st.session_state.descriptions[i] = st.text_input(
            f"Enter description for Segment {i + 1}:",
            value=st.session_state.descriptions[i]
        )

    # conditions for stories
    if st.button("Generate Story"):
        valid_descriptions = [desc.strip() for desc in st.session_state.descriptions[:num_boxes] if desc.strip()]

        if len(valid_descriptions) != num_boxes:
            st.error("Please fill all description boxes!")
        else:
            st.subheader("Generated Story")
            for i, desc in enumerate(valid_descriptions):
                with st.container():
                    st.markdown(f"**Story Page {i + 1}:** {desc}")
                    image = generate_image(desc, client)
                    st.image(image, caption=f"Segment {i + 1}: {desc}", use_container_width=True)

def main():
    st.title("Dynamic AI Query App")

    # Tabs for text and image generation
    tab1, tab2, tab3 = st.tabs(["Text Generation", "Image Generation", "Under test/Coming soon"])

    with tab1:
        text_generation_app(chat_session)

    with tab2:
        image_generation_app(image_client)
        # st.header("Image Generation")
        # user_input_image = st.text_input("Enter your description for image generation:")
        # if st.button("Generate Image"):
        #     if user_input_image.strip():
        #         output = generate_image(user_input_image, image_client)
        #         st.image(output, caption="Generated Image", use_container_width=True)
        #     else:
        #         st.error("Please enter a valid description!")
    with tab3:
        st.header("Thinking about more ideas")

if __name__ == "__main__":
    main()
