import streamlit as st
from PIL import Image
import pytesseract
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to extract text from image
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# Streamlit app
st.title("Text Extraction and Summarization")
st.write("Upload an image to extract text and optionally summarize it.")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Optional: Configure OpenAI API
openai_api_key = openai_api_key

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)


    # Extract text
    st.write("Extracting text...")
    extracted_text = extract_text_from_image(image)
    st.write("### Extracted Text:")
    st.text_area("Extracted Text", extracted_text, height=200)

    # Summarize text if API key is provided
    if openai_api_key and extracted_text.strip():
        st.write("Summarizing text...")
        llm = OpenAI(api_key=openai_api_key, temperature=0) ##The temperature=0 parameter controls the randomness of the model’s output,also use any model in this line by default it take gpt-3
        prompt_template = "Summarize the following text:\n\n{text}\n\nSummary:"
        prompt = PromptTemplate(input_variables=["text"], template=prompt_template)
        chain = LLMChain(llm=llm, prompt=prompt)

        summary = chain.run(text=extracted_text)
        st.write("### Summary:")
        st.write(summary)
