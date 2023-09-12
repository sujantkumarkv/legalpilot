# !pip install pandas
# !wget https://raw.githubusercontent.com/sujantkumarkv/legalpilot/main/indian_legal_corpus.jsonl
# !mkdir embeddings
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
def embeddings_df(lines):
    embeddings = []
    for line in lines:
        data = json.loads(line)
        text = data['text']
        embedding = query(text)
        embeddings.append(embedding)
    # convert & store temporarily as dataframe
    embeddings_df = pd.DataFrame(ipc_embeddings)
    return embeddings_df

# convert embeddings to pickle, then save it in a directory structure.

ilc_embeddings = pd.DataFrame() # indian_legal_corpus(ilc) embeddings

with open('indian_legal_corpus.jsonl', 'r') as file:
    lines = file.readlines()
    
# embeddings with each 4096 chunk
embeddings_df = embeddings_df(lines)
# append the new df to the combined df (iteratively)
ilc_embeddings = pd.concat([ilc_embeddings, embeddings_df], ignore_index=True)

combined_df.to_pickle('ilc_embeddings.pkl')
