# AI Quiz Generator

## Description
AI Quiz Generator is an intelligent tool that allows you to generate quizzes from any PDF document. Whether you need a multiple-choice quiz, yes/no questions, or short answer questions, our AI-powered system has got you covered.

🚀 **Key Features:**
- Generate quizzes from PDFs with AI verification for answers.
- Choose between multiple quiz formats: multiple-choice, yes/no, or short-answer.
- Option to process images from the PDF alongside text for enhanced question generation.
- Handles long PDFs efficiently using advanced summarization techniques.

## Technologies Used
- **FastAPI** - Backend API framework.
- **Streamlit** - Interactive frontend for quiz generation.
- **LangChain** - AI-driven text processing and quiz generation.
- **PyMuPDF** - PDF parsing and text/image extraction.
- **llama-3.3-70b-versatile** - AI-powered question generation and answer verification located in Groq Cloud

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

Now you can upload a PDF, select the quiz type, and generate your AI-powered quiz! 🎉

