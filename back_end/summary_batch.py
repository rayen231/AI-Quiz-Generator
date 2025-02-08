from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from langchain.tools import Tool
import json
from langchain.chains import LLMSummarizationCheckerChain
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

class DataSummarizerAgent:
    def __init__(self, api_key: str):
        # Initialisation du modèle LLM
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=api_key,
        )
        # Configuration de la chaîne de résumé
        self.summary_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """Vous êtes un expert en résumé. Votre tâche est de résumer de manière concise les données fournies. Le résumé doit comporter exactement deux lignes, chacune se terminant par un saut de ligne, et ne doit contenir aucune information supplémentaire ou formatage particulier.
                """
            ),
            (
                "user",
                "Données: {data}"
            )
        ])
        self.summary_chain = LLMChain(prompt=self.summary_prompt, llm=self.llm)

        # Définition de l'outil de résumé qui utilisera la chaîne summary_chain
        self.summary_tool = Tool(
            name="Résumé des données",
            func=lambda data: self.summary_chain({"data": data})['text'],
            description="Fournit un résumé en deux lignes des données fournies."
        )

# Example usage
# if __name__ == "__main__":
#     api_key = "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"  # Replace with your actual API key
#     agent = DataSummarizerAgent(api_key=api_key)
#     user_query = """Speaker diarization is the task of determining ’who spoke when’ in an audio
# segment. Since the breakthrough of deep learning, speech technology has
# experienced a huge improvement in a wide range of metrics and fields, and
# speaker diarization is no different. This thesis aims to evaluate how a state
# of the art speaker diarization system, pyannote, performs when applied to
# more difficult acoustic environments, and to investigate how that performance
# can be improved, as well as discuss what acoustic environments are difficult
# to diarize. Pyannote initially struggled to diarize audio with a lot of
# reverberations, and audio where the sound quality was considerably lower,
# such as a phone call. By utilizing fine-tuning techniques and a technique
# for augmenting the training data, the performance was greatly improved for
# the most difficult environments, and remained fairly static for the easier ones,
# implying that pyannote is robust and able to adapt to significant variations in
# the audio signal."""
#     result=agent.summary_chain({"data": user_query})['text']
#     print("summary_result :" ,result)