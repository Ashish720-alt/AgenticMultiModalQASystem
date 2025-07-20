from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0)

def parse_question(state):
    prompt = f"Analyze this question and determine what the user is asking: {state['user_question']}. Respond concisely."
    # llm.predict internally wraps the prompt as a message, sends it to the model, and returns the model's raw text response as a string.
    response = llm.predict(prompt)
    state["parsed_question"] = response
    return state
