import time
t1 = time.time()

#---------------------------------- HuggingFace API ----------------------------------------#
import requests
import json
import pandas as pd

model_id = "sujantkumarkv/legalpilot-7b-india-v1.0" # sentence-transformers/all-MiniLM-L6-v2 # sujantkumarkv/legalpilot-7b-india-v1.0
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

# Get embeddings for each line in ipc.jsonl and store in a dataframe
with open('indian_legal_corpus.jsonl', 'r') as jsonlines:
    for line in jsonlines:
        text = json.loads(line)['text']
        embedding = query(text)
        t2 = time.time()
        print("embedding done")
        break

print(f"Time: {t2-t1}s")

#-------------------------------------------------------------------------------------#