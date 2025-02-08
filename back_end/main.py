from fastapi import FastAPI, UploadFile, File ,Form
from pydantic import BaseModel
from typing import List
import os
from extract_info_from_pdf import extract_pdf_content
from quiz_based_on_pdfqcm import QuizMakerAgent_qcm as QuizMakerAgent_qcm
from quiz_based_on_pdf_on_short_question import QuizMakerAgent_ShortQuestion as QuizMakerAgent_short_question
from quiz_based_on_YesNo import QuizMakerAgent as QuizMakerAgent_YesNo
from get_image_description import PictureAnalyser
import uvicorn
from summary_batch import DataSummarizerAgent
from correct_question import AnswerCheckerAgent
import os
from fastapi.middleware.cors import CORSMiddleware
from get_image_description import check_image_size

api_key = os.getenv("API_KEY")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuizResponse(BaseModel):
    responses: List[dict]

@app.post("/quiz")
async def create_quiz(
    file: UploadFile = File(...),
    difficulty: str = Form("medium"),
    include_image: bool = Form(False),
    prefered_question: str = Form("QCM")  # Ensure this matches the key in the request
):
    # Save the uploaded PDF file
    print("saving file:",file.filename,".........")
    pdf_path = f"temp_{file.filename}"
    with open(pdf_path, "wb") as buffer:
        buffer.write(file.file.read())
    # Extract content from the PDF
    text_dict, image_dict = extract_pdf_content(pdf_path, "output_images")

    if include_image:
        if image_dict not in [None, []]:
            # Get a description of the first image in the PDF
            for image_page in image_dict.keys():
                for image_path in image_dict[image_page]:
                    # Check image size and resize if necessary
                    image_path = check_image_size(image_path)
                    image_description = PictureAnalyser(image_path)
                    text_dict[image_page] += "\n cette page contain une image avec cette description" + image_description

    print("summarizing text......")
    # Summarize each page if the PDF has more than 1 page
    agent = DataSummarizerAgent(api_key=api_key)
    if len(text_dict) > 1:
        summarized_text_dict = {}
        for page_num, text in text_dict.items():

            summary = agent.summary_chain({"data": text})['text']  # Assuming summarize_text is a function that summarizes the text
            summarized_text_dict[page_num] = summary
            print(f"Page {page_num} summarized")

        text_dict = summarized_text_dict

    print("creating quiz questions......")
    print("prefered question type:",prefered_question)
    # Initialize the QuizMakerAgent
    if prefered_question     == "QCM":
        quiz_maker = QuizMakerAgent_qcm(api_key = api_key)
    elif prefered_question == "Short Question":
        quiz_maker = QuizMakerAgent_short_question(api_key = api_key)
    elif prefered_question == "Yes/No":
        quiz_maker = QuizMakerAgent_YesNo(api_key = api_key)

    # Generate quiz questions based on the extracted content and difficulty
    quiz_questions = []
    combined_text = ""
    page_count = 0

    for page_num, text in text_dict.items():
        combined_text += text + "\n"
        page_count += 1

        if page_count == 5:
            quiz_questions.append(quiz_maker.quiz_chain({"data": combined_text,"difficulty":difficulty})['text'])
            combined_text = ""
            page_count = 0

    # If there are remaining pages that are less than 5
    if combined_text:
        quiz_questions.append(quiz_maker.quiz_chain({"data": combined_text,"difficulty":difficulty})['text'])

    print("quiz questions created :",quiz_questions)
    print("cleaning the cache......")
    # Clean up the temporary PDF file
    os.remove(pdf_path)

    # Clean up the output_images folder
    image_folder = "output_images"
    if os.path.exists(image_folder):
        for file in os.listdir(image_folder):
            file_path = os.path.join(image_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
    return {"quiz_questions": quiz_questions}

@app.post("/correct")
async def correct_quiz(response: QuizResponse):
    # Correct the quiz based on the user responses
    results = {}
    for idx, resp in enumerate(response.responses, start=1):
        user_response = resp["user_response"]
        correct_response = resp["correct_response"]
        question = resp["question"]
        # Initialize the AnswerCheckerAgent
        answer_checker = AnswerCheckerAgent(api_key=api_key)
        result = answer_checker.check_chain({"user_response": user_response, "correct_answer": correct_response, "question": question})['text']
        results[f"question{idx}"] = result
    # Compare user responses with correct responses
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
