import PyPDF2
import re
import os 

start_dir = '../../data/acts'
output_dir = '../../data_text/acts_text'

def pdf_to_txt(pdf_file):
    pdf_file_obj = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    full_text = []
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text = page_obj.extract_text()
        text = text.replace('\r', '')
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        full_text.append(text)
    print(f"{pdf_file} done.")
    return '\n'.join(full_text)



for foldername, subfolders, filenames in os.walk(start_dir):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        _, ext = os.path.splitext(file_path)
        if ext == '.pdf':
            text = pdf_to_txt(file_path)
        else:
            continue
        # Construct the new file path in the output directory
        new_folder = foldername.replace(start_dir, output_dir, 1)
        # Create directories, if they don't exist
        os.makedirs(new_folder, exist_ok=True)
        new_file_path = os.path.join(new_folder, filename.split('.')[0] + '.txt')
        # Write the text to the new file
        with open(new_file_path, 'w', errors='ignore') as new_file:
            new_file.write(text)


    
    