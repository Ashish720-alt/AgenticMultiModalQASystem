from graph import app
import json

def print_terminal_and_file(*args, **kwargs):
    text = ' '.join(str(arg) for arg in args)
    print(text, **kwargs)  # print to terminal
    with open("output.txt", "a") as f:
        f.write(text + "\n")
        
        
# Open and load the JSON file
with open('input_states/input_states.json', 'r') as f:
    input_states = json.load(f)

# 'data' is now a Python list of dictionaries
print(f"Successfully loaded {len(input_states)} items.")

for state in input_states[:5]:
    initial_state = state

    result = app.invoke(initial_state)

    query = state["user_question"]
    image_path = state["image_pat"]
    # context = state["external_facts"]
    response = result["image_caption"]

    print_terminal_and_file( f"For the query {query} on image {image_path}, we get the answer: {response}\n")
    
    