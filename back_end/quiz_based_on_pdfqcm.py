from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from langchain.tools import Tool
import json
from langchain.chains import LLMSummarizationCheckerChain
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

class QuizMakerAgent_qcm:
    def __init__(self, api_key: str):
        # Initialisation du modèle LLM
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=api_key,
        )
        # Configuration de la chaîne de détection des émotions
        self.quiz_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """Vous êtes un créateur de quiz expert. Votre tâche est de générer un quiz basé sur les données fournies et le niveau de difficulté spécifié. Le quiz doit comporter un titre et une liste de questions. Chaque question doit être courte et de type QSM (question à choix simple)

Le résultat final doit être **strictement** au format JSON, exactement comme dans l'exemple ci-dessous. **Assurez-vous que la réponse soit un objet JSON valide qui commence par curly brackets et se termine par curly brackets, sans aucun texte supplémentaire, espaces ou commentaires.**

Exemple de format attendu de question QCM :
curly_brackets
  "title": "Titre du Quiz",
  "type": "QCM",
  "questions": [
      curly_brackets"question": "Texte de la question","options":["option1","option2","option3"] , "answer": "Réponse correspondante" end_curly_brackets,
       curly_brackets"question": "Texte de la question","options":["option1","option2","option3"] , "answer": "Réponse correspondante" end_curly_brackets
  ]
end_curly_brackets

Répondez UNIQUEMENT avec ce format JSON.
                """
            ),
            (
                "user",
                "Données: {data}\nNiveau de difficulté: {difficulty}"
            )
        ])
        self.quiz_chain = LLMChain(prompt=self.quiz_prompt, llm=self.llm)


       # Définition de l'outil de création de quiz qui utilisera la chaîne quiz_chain
        self.quiz_tool = Tool(
            name="Création de Quiz",
            func=lambda difficulty,user_query:self.quiz_chain({"input": user_query,"difficulty":difficulty})['text'],
            description="Génère un quiz basé sur les données fournies et le niveau de difficulté."
        )
# Example usage
# if __name__ == "__main__":
#     api_key = "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"  # Replace with your actual API key
#     agent = QuizMakerAgent_qcm(api_key=api_key)
#     user_query = """Speaker diarization, which entails dividing a single audio recording into numerous voice recordings that each belong to a different speaker, is an essential step in working with audio data. Diarization systems do not recognize the speakers themselves; instead, they use unsupervised algorithms to segment audio recordings and organize utterances into speaker-specific categories. While voice-based biometric systems can recognize people, they can only be used for recordings with a single speaker. In this paper, an architecture for segment- or group-level single speaker diarization systems is proposed. The findings of the proposed algorithm's evaluation on the VoxCeleb and RAVDESS datasets, two speech databases, demonstrate that the group- level method outperforms the segment-level strategy in terms of recognition results. The difficulty of detecting numerous speakers chatting freely in an audio recording while accounting for emotional swings that may impact speech patterns is addressed in these systems, which show promise. According to the study, diarization can obtain accuracy levels of over 95.4 percent when applied to the RAVDESS and VoxCeleb datasets, which suggests that the suggested approach from speech can achieve levels of accuracy of over 96.4 percent."""
#     difficulty="Moyen"
#     prefered_question="QCM"
#     quiz_result=agent.quiz_chain({"data": user_query,"difficulty":difficulty})['text']
#     print("quiz_result :" ,quiz_result)
#     quiz_dict = json.loads(quiz_result)
#     print(quiz_dict)