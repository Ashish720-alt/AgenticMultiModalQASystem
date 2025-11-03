# agents/answer_agent.py
import warnings
import os
from huggingface_hub import InferenceClient

warnings.filterwarnings("ignore", category=UserWarning, module="langchain_community")

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise EnvironmentError("Missing HF token. Set HF_TOKEN or HUGGINGFACEHUB_API_TOKEN.")

MODEL_ID = "HuggingFaceH4/zephyr-7b-alpha"
client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

def generate_answer(context: str, question: str = None) -> dict:
    """
    Generates a concise answer using the provided context and question.
    If question is None, attempts to read it from the context (graph state).
    Returns a dict for LangGraph compatibility.
    """
    try:
        # If only one argument was provided (LangGraph passing a dict)
        if isinstance(context, dict):
            question = context.get("question", question)
            context = context.get("context", str(context))

        if not question:
            question = "What does this image or context represent?"

        prompt = (
            f"Context:\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Answer clearly and concisely."
        )

        response = client.chat_completion(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a concise and accurate assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=256,
            temperature=0.3,
            top_p=0.9,
        )

        text = response.choices[0].message["content"].strip()
        return {"final_answer": text}   # ✅ return dict
    except Exception as e:
        return {"final_answer": f"[Answer Agent Error] {e}"}
