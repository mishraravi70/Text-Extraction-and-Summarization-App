# Text Extraction and Summarization App

This application allows users to upload an image, extract text from it, and optionally summarize the extracted text using OpenAI's language models. It is built using **Streamlit**, **Pillow**, **Pytesseract**, and **LangChain**.

---

## Features

1. **Image Upload**: Upload images in PNG, JPG, or JPEG formats.
2. **Text Extraction**: Extract text from the uploaded image using Pytesseract.
3. **Text Summarization**: Summarize the extracted text using OpenAI's API (if an API key is provided).

---

## How to Use

1. **Install Dependencies**:
   Ensure you have Python installed and install the required libraries:
   ```bash
   pip install streamlit pillow pytesseract langchain openai
   ```

2. **Set Up OpenAI API Key**:
   Export your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```

3. **Run the App**:
   Execute the following command to start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. **Upload an Image**:
   - Use the file uploader to select an image.
   - The app will display the uploaded image and extract its text.

5. **View Extracted Text**:
   - The extracted text will be displayed in a text area for review.

6. **Summarize Text** (Optional):
   - If the OpenAI API key is configured and the extracted text is non-empty, the app will provide a summarized version of the text.

---

## Code Overview

### Main Components

- **Image Upload**:
  ```python
  uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
  ```

- **Text Extraction**:
  ```python
  def extract_text_from_image(image):
      text = pytesseract.image_to_string(image)
      return text
  ```

- **Summarization**:
  ```python
  llm = OpenAI(api_key=openai_api_key, temperature=0)
  prompt_template = "Summarize the following text:\n\n{text}\n\nSummary:"
  prompt = PromptTemplate(input_variables=["text"], template=prompt_template)
  chain = LLMChain(llm=llm, prompt=prompt)
  summary = chain.run(text=extracted_text)
  ```

---

## Requirements

- Python 3.7+
- Dependencies:
  - **Streamlit** (latest version: 1.25.0)
  - **Pillow** (latest version: 10.0.0)
  - **Pytesseract** (latest version: 0.3.10)
  - **LangChain** (latest version: 0.0.330)
  - **OpenAI** (latest version: 0.27.10)

---

## Notes

- **Tesseract Installation**: Ensure that Tesseract is installed on your system. Refer to the [Tesseract documentation](https://github.com/tesseract-ocr/tesseract) for installation instructions.
- **OpenAI API Key**: The summarization feature requires a valid OpenAI API key. Without it, only text extraction will be available.
- **Temperature Setting**: The `temperature=0` parameter controls the randomness of the OpenAI model's output, ensuring deterministic results.

---

## Example Use Case

1. **Upload an Image**:
   ![Sample Uploaded Image](example-image.png)

2. **Extracted Text**:
   ```
   This is an example of extracted text from the image.
   ```

3. **Summarized Text**:
   ```
   Example summary of the extracted text.
   ```

---

## License

This project is open-source and available under the MIT License.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the app.



