from graph import app

initial_state = {
    "image_path": "data/sample.png",
    "user_question": "What is written on the whiteboard?" #Or get one from prompts/question.txt
}

result = app.invoke(initial_state)

print("Image Caption:", result["image_caption"])