import json
import os

# List of directories to iterate through
directories = ['data_jsonl/acts_jsonl/']

# Output file
output_file = 'indian_legal_corpus.jsonl'
import os
import jsonlines

# Open the output file
with open(output_file, 'a') as outfile:
    # Iterate through each directory
    for directory in directories:
        # Iterate through each file in the directory
        for filename in os.listdir(directory):
            # Check if the file is a JSONL file
            if filename.endswith('.jsonl'):
                # Open the JSONL file
                with open(os.path.join(directory, filename), 'r') as infile:
                    # Write the entire file to the output file
                    outfile.write(infile.read())