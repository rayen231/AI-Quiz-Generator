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
- **Advanced Question Types:** Plans to include open-ended questions and essay-type queries.
- **Multi-Language Support:** Enabling multi-language PDFs to be processed and quizzes to be generated in different languages.
- **Better Model Tuning:** Ongoing improvements in model accuracy and output coherence, based on user feedback.
---
Now you can upload a PDF, select the quiz type, and generate your AI-powered quiz! 🎉
---

## Streamlit Demo : 
![image](https://github.com/user-attachments/assets/7279fb6e-5124-49c9-8c48-19cebaed6379)
![image](https://github.com/user-attachments/assets/40f73605-7adb-4af4-95ce-102b97bf2a9e)
![image](https://github.com/user-attachments/assets/3d405174-2fca-4299-b2a7-0c08725c240e)
![image](https://github.com/user-attachments/assets/b5ee21e5-1491-496e-acb1-e3e707379a2c)
![image](https://github.com/user-attachments/assets/a3b94f52-256a-40de-ac1c-3bede17f95ce)
![image](https://github.com/user-attachments/assets/49245226-5018-4a49-85da-cebede94dc3c)
![image](https://github.com/user-attachments/assets/c3253d31-25c4-44d9-b5e2-214dc88faf76)
![image](https://github.com/user-attachments/assets/cc9f5f2c-e3b1-4b2c-bdb6-2984b54e175a)
![image](https://github.com/user-attachments/assets/aebec3f5-b159-475a-9b1d-25dd8a785801)
![image](https://github.com/user-attachments/assets/ea043c77-aef5-4bc0-ba7d-ccd03e5b9ada)
![image](https://github.com/user-attachments/assets/4504e399-2ce4-44ee-821b-6eab38fb3c63)
![image](https://github.com/user-attachments/assets/f2f8ef84-19df-4277-a9c6-0a8e8c4fcf87)
![image](https://github.com/user-attachments/assets/7bf5bbfc-8d92-4662-a116-3b7ed5a5e720)
![image](https://github.com/user-attachments/assets/4b478b1c-f7e1-4bd8-862c-c07a3ab92dfe)
![image](https://github.com/user-attachments/assets/3358e80e-7d6a-4ddc-90fe-a3256d7b81ff)

## Fast Api Demo
![image](https://github.com/user-attachments/assets/b0f90e07-c7ba-4390-a58d-09861664b9e6)
![image](https://github.com/user-attachments/assets/50948e00-7ecb-47e6-9a47-6415ecd19276)
![image](https://github.com/user-attachments/assets/b367ea0f-849f-468f-8de2-160f94f41304)















