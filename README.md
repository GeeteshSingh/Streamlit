# **Dynamic AI Query App**

A Streamlit-based application that allows users to generate text and images dynamically using advanced AI models. The app is designed to streamline text-based content generation and story-like image generation in a user-friendly interface.

---

## **Features**

### Text Generation
- Generate creative and informative text responses using Google's **Gemini-2.0-Flash** generative model.
- Track search history with a sidebar display for easy access to previous queries.

### Image Generation
- Generate 2D comic-style images based on descriptive inputs.
- Create story-like image sequences (up to 4 segments) with captions.
- Dynamically adjust the number of story segments through a dropdown.

---

## **Setup and Installation**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/dynamic-ai-query-app.git
cd dynamic-ai-query-app
```

### 2. **Install Dependencies**
Ensure you have Python installed (preferably 3.9+). Install the required packages:
```bash
pip install -r requirements.txt
```

### 3. **Environment Variables**
Create a `.env` file in the root directory with the following content:
```
GENAI_API_KEY=your_genai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
- Replace `your_genai_api_key` and `your_huggingface_api_key` with your actual API keys for Generative AI and HuggingFace.

### 4. **Run the Application**
Launch the Streamlit app:
```bash
streamlit run main.py
```

---

## **Project Structure**
```
dynamic-ai-query-app/
│
├── main.py                   # Main script to run the app
├── text_generation.py        # Text generation logic
├── image_generation.py       # Image generation logic
├── utils.py                  # Shared initialization functions for AI models
├── requirements.txt          # Python dependencies
├── .env                      # API keys (ignored in Git)
└── README.md                 # Project documentation
```

---

## **How to Use**

### **1. Text Generation**
- Navigate to the **Text Generation** tab.
- Enter a query in the text area and click **Generate Now!**.
- The AI will respond with a creative answer, which will also be saved in the **Your Search History** section in the sidebar.

### **2. Image Generation**
- Navigate to the **Image Generation** tab.
- Select the number of story segments (1–4) from the dropdown.
- Provide descriptions for each story segment.
- Click **Generate Story** to create a sequence of 2D comic-style images with captions.

#### Example:
- **Description 1:** A man sitting on a chair  
- **Description 2:** The man is eating lunch  
- **Description 3:** The man enjoying lunch happily  

The app will generate a sequence of comic-style images to visualize this short story.

---

## **Technologies Used**
- **[Streamlit](https://streamlit.io/):** For building the interactive web app.
- **[Google Generative AI](https://developers.generativeai.google/):** For text generation (Gemini-2.0-Flash model).
- **[HuggingFace Hub](https://huggingface.co/):** For image generation (Stable Diffusion 3.5 model).
- **[Python](https://www.python.org/):** Core programming language.
- **[dotenv](https://pypi.org/project/python-dotenv/):** For managing environment variables.

---

## **Requirements**
- Python 3.9+
- `GENAI_API_KEY` for Google Generative AI
- `HUGGINGFACE_API_KEY` for HuggingFace Image generation

---

## **Future Improvements**
- Support for more story segments (beyond 4).
- Add functionality for real-time editing of generated text or images.
- Explore additional AI models for more varied outputs.
- Add an **export feature** to save generated content (text + images) as a PDF or slideshow.

---

## **Contributing**
Contributions are welcome! Follow these steps:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License.

---

## **Contact**
For any issues or suggestions, feel free to reach out:
- **Email:** singh.geetesh1998@gmail.com
- **GitHub:** [My Profile](https://github.com/geeteshsingh)
