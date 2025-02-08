from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from langchain.tools import Tool
import json
from langchain.chains import LLMSummarizationCheckerChain
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

class AnswerCheckerAgent:
        def __init__(self, api_key: str):
        # Initialisation du modèle LLM
            self.llm = ChatGroq(
                model="gemma2-9b-it",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                api_key=api_key,
            )
            # Configuration de la chaîne de vérification des réponses
            self.check_prompt = ChatPromptTemplate.from_messages([
                (
                "system",
                """Vous êtes un correcteur de réponses expert. Votre tâche est de comparer la réponse de l'utilisateur avec la réponse correcte et baseé sur le question et de renvoyer **uniquement** True ou False.

Instructions :
- Si la réponse de l'utilisateur correspond exactement ou est très proche de la réponse correcte, renvoyez **True**.
- Sinon, renvoyez **False**.
- Répondez **uniquement** avec True ou False, sans aucun texte supplémentaire.
                """
            ),
            (
                "user",
                "Réponse utilisateur: {user_response}\nRéponse correcte: {correct_answer} \n question : {question}"
            )
        ])

            self.check_chain = LLMChain(prompt=self.check_prompt, llm=self.llm)

        # Définition de l'outil de vérification de réponse
            self.check_tool = Tool(
                name="Vérification de réponse",
                func=lambda user_response, correct_answer: self.check_chain({
                    "user_response": user_response,
                    "correct_answer": correct_answer
                })['text'].strip(),
                description="Compare la réponse de l'utilisateur avec la réponse correcte et renvoie True ou False."
            )

# Example usage
# if __name__ == "__main__":
#     api_key = "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"  # Replace with your actual API key
#     agent = AnswerCheckerAgent(api_key=api_key)
#     quiz_result=agent.check_chain({"user_response":" is to trancribe audio to text ","correct_answer":"transcribe is to identify who speaks in an audio to classify the speakers","question":" what is speaker dirization"})['text']
#     print("response",quiz_result)