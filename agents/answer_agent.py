from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import config as conf

if (conf.LLM_model == conf.GOOGLE):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=conf.TEMP) 
else:
    llm = ChatOpenAI(model="gpt-4", temperature=conf.TEMP)

def generate_answer(state):
    prompt = f"""Based on the image caption: "{state['image_caption']}", 
    and external knowledge: "{state.get('external_facts', '')}", 
    answer the question: "{state['user_question']}"."""
    
    response = llm.predict(prompt)
    state["final_answer"] = response
    return state