import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os


# Loading env
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


def initialize_image_client():
    return InferenceClient(
        "stabilityai/stable-diffusion-3.5-large",
        token=HUGGINGFACE_API_KEY,
    )


def generate_image(description, client):
    comic_style_description = (f"{description.strip()}, in 2D comic style, cartoon-like, vibrant colors, and minimal "
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
