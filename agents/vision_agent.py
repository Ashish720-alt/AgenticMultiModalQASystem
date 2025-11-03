# agents/vision_agent.py
import os
import warnings
from huggingface_hub import InferenceClient

warnings.filterwarnings("ignore", category=UserWarning, module="langchain_community")

# ✅ Get token automatically from environment
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise EnvironmentError("Missing HF token. Set HF_TOKEN or HUGGINGFACEHUB_API_TOKEN.")

# ✅ Use Zephyr (chat model)
MODEL_ID = "HuggingFaceH4/zephyr-7b-alpha"

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

def analyze_image(image_description: str) -> dict:
    """
    Uses a lightweight Hugging Face chat model to describe the image textually.
    Returns a dict for LangGraph compatibility.
    """
    try:
        prompt = (
            f"You are an intelligent vision assistant. "
            f"Given this description of an image:\n\n"
            f"'{image_description}'\n\n"
            f"Describe what this image likely contains in detail. "
            f"Focus on objects, relationships, and possible context."
        )

        response = client.chat_completion(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a concise, helpful visual reasoning assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=256,
            temperature=0.3,
            top_p=0.9,
        )

        text = response.choices[0].message["content"].strip()
        return {"vision_output": text}   # ✅ return dict instead of string
    except Exception as e:
        return {"vision_output": f"[Vision Agent Error] {e}"}
