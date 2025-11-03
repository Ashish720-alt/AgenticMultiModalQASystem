from graph import app
import json, time
import graphConfig as conf

def log(*args):
    text = ' '.join(str(a) for a in args)
    print(text)
    with open("output.txt", "a") as f:
        f.write(text + "\n")

start = time.time()

with open('input_states/input_states.json', 'r') as f:
    states = json.load(f)[:conf.BENCHMARK_INPUTS] 

log(f"Running {len(states)} image-question pairs ...\n")

for i, s in enumerate(states, 1):
    try:
        res = app.invoke(s)
        ans = res.get("final_answer", "No answer")
        log(f"[{i}] Q: {s['user_question']}\nImage: {s['image_path']}\nA: {ans}\n{'-'*80}")
    except Exception as e:
        log(f"[{i}] ERROR: {e}\n")

log(f"Completed in {time.time()-start:.1f}s.")
