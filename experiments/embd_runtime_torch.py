# wget https://raw.githubusercontent.com/sujantkumarkv/legalpilot/main/experiments/embd_runtime_torch.py

import time
t1 = time.time()
#--------------------------------- Model download & pytorch -----------------------------------#
import json
import torch
from transformers import AutoTokenizer, AutoModel

model_id = "sujantkumarkv/legalpilot-7b-india-v1.0" # "tiiuae/falcon-rw-1b" # sujantkumarkv/legalpilot-7b-india-v1.0 # NousResearch/Llama-2-7b-hf

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id, output_hidden_states=True)
t2 = time.time() # time to load model

with open('indian_legal_corpus.jsonl', 'r') as jsonlines:
    for line in jsonlines:
        text = json.loads(line)['text']
        break

tokens = tokenizer(text, return_tensors="pt")

with torch.no_grad():
  outputs = model(**tokens)

# print(type(outputs))
# print(outputs.last_hidden_state)
# print(outputs[0].shape)

embeddings = outputs.last_hidden_state
t3 = time.time()

print(f"Time to load model: {t2-t1}s")
print(f"Time for embeddings: {t3-t2}s")

#-------------------------------------------------------------------------------------#