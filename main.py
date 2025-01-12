import streamlit as st

from text_generation import text_generation_app, initialize_text_model
from image_generation import image_generation_app, initialize_image_client

# Initialize models
text_model = initialize_text_model()
chat_session = text_model.start_chat(history=[])
image_client = initialize_image_client()


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
