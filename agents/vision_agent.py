from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from PIL import Image
import base64

llm = ChatOpenAI(model="gpt-4-vision-preview")

def analyze_image(state):
    with open(state["image_path"], "rb") as img_file:
        image_bytes = img_file.read()
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    
    prompt = "Describe the contents of this image in detail."
    msg = HumanMessage(content=[{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}])
    
    response = llm([msg])
    state["image_caption"] = response.content
    return state