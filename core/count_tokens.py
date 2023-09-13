import os

output_dir = "../data/legal_drafts_text"
encodings_to_try = ['utf-8', 'ISO-8859-1', 'cp1252']

ct = 0
total = 0
for foldername, subfolders, filenames in os.walk(output_dir):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        total += 1
        # 100 tokens -> 75 words
        for encoding in encodings_to_try:
            try:
                with open(file_path, 'r', encoding=encoding) as inFile:
                    text = inFile.read()
                    tokens = int(len(text.split()) * 4/3) # 100 tokens -> 75 words
                    if tokens> 1800:
                        ct += 1
                        print(f"{file_path} has {tokens} tokens")
                break
            except UnicodeDecodeError:
                continue

print(f"% of files with more than 1800 tokens: {ct * 100 / total} or {ct}/{total} files")




    

