from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import config as conf

if (conf.LLM_model == conf.GOOGLE):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0) #Temperature 0 means not random!
else:
    llm = ChatOpenAI(model="gpt-4", temperature=0)

def generate_answer(state):
    prompt = f"""Based on the image caption: "{state['image_caption']}", 
    and external knowledge: "{state.get('external_facts', '')}", 
    answer the question: "{state['user_question']}"."""
    
    response = llm.predict(prompt)
    state["final_answer"] = response
    return state