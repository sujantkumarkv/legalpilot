# from transformers import AutoTokenizer
import sentencepiece
import json
import os

tokenizer = sentencepiece.SentencePieceProcessor(model_file='llama2_tokenizer/tokenizer.model')

def tokenize_text(tokenizer, text):
    """
    Tokenize the given text using a tokenizer function.
    This function is a placeholder; plug in SentencePiece or Hugging Face tokenization here.
    """
    tokens = tokenizer.encode(text)
    return tokens

def chunk_text(tokens, chunk_size=4000, overlap=32): # 4096 overflows somehow;
    """
    Splits a list of tokens into smaller chunks based on a given size and overlap.
    """
    chunks = []
    start_idx = 0
    while start_idx < len(tokens):
        end_idx = start_idx + chunk_size
        chunks.append(tokens[start_idx: end_idx])
        start_idx = end_idx - overlap

        # If the remaining tokens are less than the chunk size, break the loop
        if len(tokens) - start_idx <= chunk_size:
            break

    chunks.append(tokens[start_idx: ]) # append the remaining tokens
    chunks_text = [tokenizer.decode(chunk) for chunk in chunks]
    return chunks_text
    

def write_jsonl(chunks, output_file):
    """
    Writes a list of chunks to a JSONL file.
    """
    with open(output_file, 'w') as f:
        for chunk in chunks:
            # half = len(chunk) // 2
            # input_chunk = str(chunk[: half])
            # target_chunk = str(chunk[half: ])
            text = str(chunk)
            # json_obj = {"input": "".join(input_chunk), "target": "".join(target_chunk)}
            json_obj = {"text": "".join(text)}
            f.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

# Read text from a file (this is an example; you'll read from an actual text file)
# textfile = '../data_text/constitution.txt'
# with open(textfile, 'r') as f:
#     text = f.read()

# # Tokenize text
# tokens = tokenize_text(tokenizer=tokenizer, text=text)

# # Chunk tokens
# chunks_text = chunk_text(tokens)

# write_jsonl(chunks_text, "../data_jsonl/constitution.jsonl")

# ########## iterating for all files (to jsonl)
start_dir = '../data_text/acts_text'
output_dir = '../data_jsonl/acts_jsonl'

for foldername, subfolders, filenames in os.walk(start_dir):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        with open(file_path, 'r') as infile:
            text = infile.read()

        # Construct the new file path in the output directory
        new_folder = foldername.replace(start_dir, output_dir, 1)
        # Create directories, if they don't exist
        os.makedirs(new_folder, exist_ok=True)
        new_file_path = os.path.join(new_folder, filename.split('.')[0] + '.jsonl')

        # tokens of the file
        tokens = tokenize_text(tokenizer=tokenizer, text=text)
        # Chunk tokens
        chunks_text = chunk_text(tokens)
        # Write the text to the new file
        write_jsonl(chunks_text, new_file_path)

