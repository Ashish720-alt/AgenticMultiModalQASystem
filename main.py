from graph import app
import json

# Open and load the JSON file
with open('input_states/input_states.json', 'r') as f:
    input_states = json.load(f)

# 'data' is now a Python list of dictionaries
print(f"Successfully loaded {len(input_states)} items.")

for state in input_states[:5]:
    initial_state = state

    result = app.invoke(initial_state)

    print("Image Caption:", result["image_caption"])