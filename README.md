# Agentic Multi-Modal QA System 🤖🖼️

A multi-agent system built with **LangGraph** and **LangChain**, capable of answering complex questions about images and text using **Hugging Face models**.  
Each agent performs a distinct role — vision analysis, question parsing, knowledge retrieval, and answer generation.

---

## 🧩 Architecture
image → Vision Agent → Question Agent → Knowledge Agent → Answer Agent

yaml
Copy code

- **Vision Agent** – analyzes the input image (via Hugging Face vision models).  
- **Question Agent** – interprets user queries and transforms them into reasoning-ready prompts.  
- **Knowledge Agent** – retrieves supporting facts or background info using DuckDuckGo.  
- **Answer Agent** – synthesizes the final answer via an LLM.

---

## ⚙️ Setup Instructions

### 1️⃣ Create Environment
Run the following commands to set up the environment:
conda env create -f environment.yml  
conda activate langgraph-env  

### 2️⃣ Set Hugging Face Token
You must have a valid Hugging Face token for API access. Export it as an environment variable:
export HF_TOKEN=hf_your_token_here  
export HUGGINGFACEHUB_API_TOKEN=$HF_TOKEN  

### 3️⃣ Run the System
Execute the main script to start the pipeline:
python main.py  

The system automatically processes all image–question pairs in the `inputs/` directory and writes outputs to `output.txt`.

---

## 🧠 Notes
- Default model: **HuggingFaceH4/zephyr-7b-alpha**  
- You can switch to smaller, cheaper models (e.g. `mistralai/Mistral-7B-Instruct-v0.2`) in `question_agent.py` or `vision_agent.py`.  
- All `LangChainDeprecationWarning` messages are suppressed in code.  
- The project avoids PyTorch/NVIDIA dependencies and runs fully via **Hugging Face Inference API**.

---

## 🧰 Troubleshooting
If you encounter:  
LangChainDeprecationWarning: The class `HuggingFaceEndpoint` was deprecated...  
→ Safe to ignore (warnings are filtered).  

If you get:  
ValueError: Model not supported for task text-generation...  
→ Use a model that supports `text-generation` or `conversational` tasks.


## 📁 Directory Structure

agents/  
&nbsp;&nbsp;├── vision_agent.py  # Image captioning / understanding  
&nbsp;&nbsp;├── question_agent.py # Question interpretation  
&nbsp;&nbsp;├── knowledge_agent.py # Web/text retrieval  
&nbsp;&nbsp;└── answer_agent.py  # Final synthesis step  

graph.py      # Defines LangGraph workflow  
main.py      # Entry point  
inputs/      # Image and question data  
output.txt     # Generated answers  
environment.yml  # Conda environment file  
README.md     # Project documentation  

---

**Author:** Ashish Kumar  
**Purpose:** Research prototype for multi-modal agentic reasoning using open-source language and vision models.
