# AI Quiz Generator

## Description
AI Quiz Generator is an intelligent tool that allows you to generate quizzes from any PDF document. Whether you need a multiple-choice quiz, yes/no questions, or short answer questions, our AI-powered system has got you covered.

🚀 **Key Features:**
- **AI-Verified Answers:** Automatically generates and verifies answers for each question.
- **Multiple Quiz Formats:** Supports multiple question types, including multiple-choice, yes/no, and short-answer.
- **Image Processing:** Extracts and processes images from PDFs to generate more comprehensive questions.
- **Long PDF Handling:** Efficiently processes lengthy documents by summarizing and analyzing text with advanced techniques.
- **Customizable Output:** Generates quizzes in a clean, structured JSON format, perfect for easy integration into various platforms.
- **LangChain & Agents:** Utilizes LangChain with agents and prompts to ensure the output is fine-tuned and coherent, with temperature control optimized based on multiple test runs.
- **High Accuracy:** Carefully tuned temperature settings ensure the generated questions are relevant, balanced, and contextually accurate.
- **Level of Difficulty:** Use the level of Difficulty that goes with you task

---

## Technologies Used
- **FastAPI:** Backend API framework for fast, asynchronous server-side operations.
- **Streamlit:** Interactive frontend for intuitive quiz generation and management.
- **LangChain:** AI-powered text processing, quiz generation, and agent orchestration.
- **PyMuPDF:** PDF parsing and extraction of text and images for enhanced quiz creation.
- **llama-3.3-70b-versatile (Groq Cloud):** Cutting-edge language model used for question generation and answer verification.
- **Temperature Control:** The model’s output temperature is finely adjusted based on multiple rounds of testing, ensuring a balance between creativity and accuracy.

---

## Installation

### Requirements
Make sure you have Python installed. You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Backend
Navigate to the backend folder and start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload
```

### Running the Frontend
Navigate to the frontend folder and start the Streamlit app:
```bash
cd frontend
streamlit run front.py
```
---
## Customization Options
**You can fine-tune the generated quizzes by adjusting parameters such as:**

- **Quiz Type:** Choose your preferred question format (multiple-choice, yes/no, or short-answer).
- **Text/Image Handling:** Control the depth of image analysis and text summarization for better question generation.
- **Difficulty :** choose hard or medium or hard ! 
---
## Future Improvements
**Advanced Question Types:** Plans to include open-ended questions and essay-type queries.
**Multi-Language Support:** Enabling multi-language PDFs to be processed and quizzes to be generated in different languages.
**Better Model Tuning:** Ongoing improvements in model accuracy and output coherence, based on user feedback.
---
Now you can upload a PDF, select the quiz type, and generate your AI-powered quiz! 🎉

