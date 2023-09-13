import json
import requests
import pandas as pd

model_id = "tiiuae/falcon-rw-1b" # "sentence-transformers/all-MiniLM-L6-v2" # "sujantkumarkv/legalpilot-7b-india-v1.0"
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()


# Read the ipc.jsonl file
with open('data_jsonl/ipc.jsonl', 'r') as file:
    lines = file.readlines()

# Get embeddings for each line in ipc.jsonl and store in a dataframe
ipc_embeddings = []

# for line in lines:
#     data = json.loads(line)
#     text = data['text']
#     embedding = query(text)
#     ipc_embeddings.append(embedding)

line = lines[0]
data = json.loads(line)
text = data['text']
embedding = query(text)
ipc_embeddings.append(embedding)


ipc_df = pd.DataFrame(ipc_embeddings)
print(ipc_df.shape)

