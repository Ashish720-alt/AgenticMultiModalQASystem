
import streamlit as st
from graph import app

st.title("🧠 Multi-Agent Photo QA System")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
question = st.text_input("Ask a question about the image")

if uploaded_file and question:
    image_path = f"data/{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    initial_state = {
        "image_path": image_path,
        "user_question": question
    }

    with st.spinner("Thinking..."):
        result = app.invoke(initial_state)
    
    st.image(image_path, caption="Uploaded Image")
    st.markdown(f"**Answer:** {result['final_answer']}")
