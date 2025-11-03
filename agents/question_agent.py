# agents/question_agent.py
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_community")
from langchain_core._api import deprecation
warnings.filterwarnings("ignore", category=deprecation.LangChainDeprecationWarning)


from langchain_community.llms import HuggingFaceEndpoint

# Uses Zephyr (text-only) for question parsing
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-alpha",
    temperature=0.2,
    max_new_tokens=256,
)

def parse_question(question_text: str) -> str:
    """
    Parses or reformulates a user's question to ensure clarity.
    """
    try:
        prompt = f"Rephrase the following question for clarity: {question_text}"
        return llm.invoke(prompt)
    except Exception as e:
        return f"[Question Agent Error] {e}"
