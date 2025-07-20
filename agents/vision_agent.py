from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import base64

llm = ChatOpenAI(model="gpt-4-vision-preview")

def analyze_image(state):
    with open(state["image_path"], "rb") as img_file:
        #Reads the image as raw bytes (raw bytes are used for .jpg, .png files eg: b'\xff\xd8\xff\xe0').
        image_bytes = img_file.read()
        #Convert it to base64-encoded string, which is how OpenAI expects image input when using image_url mode. (base 64 - encoding is a way to only use printable ASCII charactars.)
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    
    # Builds a multi-part message: 1. A text prompt 2. An embedded base64 image.
    # LangChain knows how to serialize this into the format GPT-4-Vision expects.
    prompt = "Describe the contents of this image in detail."
    # The url f"data:image/png;base64,{image_b64}" is a Base 64 Data URL i.e. a special URL which that embeds data directly in the URL itself,
    # instead of pointing to an external file or resource. You could open this url in a browswer or supported VLM.
    msg = HumanMessage(content=[{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}])
    
    # For LangChain's ChatOpenAI, response is an instance of some class which contains a content field storing the output of the LLM as a string.
    response = llm([msg])
    state["image_caption"] = response.content
    return state