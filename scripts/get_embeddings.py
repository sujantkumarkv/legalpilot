# !pip install pandas
# !wget https://raw.githubusercontent.com/sujantkumarkv/legalpilot/main/indian_legal_corpus.jsonl
# !mkdir embeddings
import requests
import json
import pandas as pd


#---------------------------------- HuggingFace API ----------------------------------------#

model_id = "sujantkumarkv/legalpilot-7b-india-v1.0" # sentence-transformers/all-MiniLM-L6-v2 # sujantkumarkv/legalpilot-7b-india-v1.0
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

# Get embeddings for each line in ipc.jsonl and store in a dataframe
def embeddings_df():
    ct = 0
    embeddings = []
    with open('indian_legal_corpus.jsonl', 'r') as jsonlines:
        for line in jsonlines:
            ct += 1
            # Each line is a valid JSON object
            text = json.loads(line)['text'] 
            embedding = query(text)
            embeddings.append(embedding)
            # if ct % 100 == 0:
            print(f"{ct} steps done")
    # convert & store temporarily as dataframe
    embeddings_df = pd.DataFrame(embeddings)
    return embeddings_df

# convert embeddings to pickle, then save it in a directory structure.
ilc_embeddings = embeddings_df()

# ilc_embeddings = pd.concat([ilc_embeddings, embeddings_df], ignore_index=True)

ilc_embeddings.to_pickle('ilc_embeddings.pkl')


#-------------------------------------------------------------------------------------#



#--------------------------------- Model download & pytorch -----------------------------------#
""" 
import torch
from transformers import AutoTokenizer, AutoModel

model_id = "tiiuae/falcon-rw-1b" # sujantkumarkv/legalpilot-7b-india-v1.0 # NousResearch/Llama-2-7b-hf

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id, output_hidden_states=True)

tokens = tokenizer(input_text, return_tensors="pt")

with torch.no_grad():
  outputs = model(**tokens)

# print(type(outputs))
# print(outputs.last_hidden_state)
# print(outputs[0].shape)

embedings = outputs.last_hidden_state
"""
#-------------------------------------------------------------------------------------#