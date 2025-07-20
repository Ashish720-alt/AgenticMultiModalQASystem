from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0)

def parse_question(state):
    prompt = f"Analyze this question and determine what the user is asking: {state['user_question']}. Respond concisely."
    response = llm.predict(prompt)
    state["parsed_question"] = response
    return state
