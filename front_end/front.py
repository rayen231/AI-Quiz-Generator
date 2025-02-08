import streamlit as st
import requests
import json

# Define API endpoints
QUIZ_API_URL = "http://44.226.145.213:8000/quiz"
CORRECT_API_URL = "http://44.226.145.213:8000/correct"

def main():
    st.title("Quiz Generator and Evaluator")

    # File Upload and Options
    uploaded_file = st.file_uploader("Upload a file for quiz generation", type=["txt", "pdf", "docx"])
    difficulty = st.selectbox("Select difficulty level", ["easy", "medium", "hard"], index=1)
    image_option = st.selectbox("Do you want the image in the pdf to be considered in quiz?", ["yes", "no"])
    prefered_question = st.selectbox("Select preferred question type", ["QCM", "Short Question", "Yes/No"], index=1)

    # Generate Quiz Section
    if uploaded_file and st.button("Generate Quiz"):
        # Prepare the file upload payload with filename and MIME type
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        # Convert boolean value to a string so that it is properly parsed by the backend
        include_image = True if image_option.lower() == "yes" else False

        with st.spinner("Waiting for the API request to generate quiz..."):
            response = requests.post(
                QUIZ_API_URL,
                files=files,
                data={
                    "difficulty": difficulty,
                    "prefered_question": prefered_question,
                    "include_image": str(include_image).lower()  # "true" or "false"
                }
            )
        
        if response.status_code == 200:
            quiz_data = response.json()
            # Assuming quiz_data["quiz_questions"] is a list of JSON strings, we load the first one
            st.session_state.quiz = json.loads(quiz_data["quiz_questions"][0])
        else:
            st.error("Failed to generate quiz.")

    # Display Quiz Questions and Submit Answers (only if a quiz is available)
    if "quiz" in st.session_state:
        st.write(f"### {st.session_state.quiz['title']}")
        responses = []
        user_answers = {}
        print(st.session_state.quiz['questions'])
        for idx, q in enumerate(st.session_state.quiz['questions']):
            # Determine the question type from the quiz data    
            quiz_type = st.session_state.quiz.get('type', 'Short Question')
            if prefered_question == "Short Question":
                answer = st.text_input(q['question'], key=f"q{idx}")
            elif prefered_question == "QCM":
                answer = st.selectbox(q['question'], q['options'], key=f"q{idx}")
            elif prefered_question == "Yes/No":
                answer = st.selectbox(q['question'], ["Yes", "No"], key=f"q{idx}")
            else:
                # Fallback to a text input if type is unknown
                answer = st.text_input(q['question'], key=f"q{idx}")
            
            user_answers[idx] = answer
            responses.append({
                "question": q['question'],
                "user_response": answer,
                "correct_response": q['answer']
            })

        if st.button("Submit Answers"):
            payload = {"responses": responses}
            with st.spinner("Waiting for the API request to evaluate responses..."):
                correction_response = requests.post(CORRECT_API_URL, json=payload)
            
            if correction_response.status_code == 200:
                correction_results = correction_response.json()
                st.write("### Quiz Results")
                correct_count = 0
                total_questions = len(responses)
                
                for idx, (key, result) in enumerate(correction_results["results"].items()):
                    st.write(f"**Question {idx+1}:** {responses[idx]['question']}")
                    st.write(f"Your Answer: {user_answers[idx]}")
                    
                    if "true" in result.lower():
                        correct_count += 1
                        st.success("Correct!")
                    else:
                        st.error("Incorrect!")
                        st.info(f"Correct Answer: {responses[idx]['correct_response']}")
                    
                    st.markdown("---")
                
                # Show score alert
                score = (correct_count / total_questions) * 100
                st.success(f"Your score: {score:.2f}%")
                
                # Provide option to download quiz as JSON with a unique key
                quiz_json = json.dumps(st.session_state.quiz, indent=4)
                st.download_button("Download Quiz as JSON", quiz_json, "quiz.json", "application/json", key="download_quiz")
            else:
                st.error("Failed to evaluate responses.")

if __name__ == "__main__":
    main()
