from pdfminer.high_level import extract_text

# Starting directory
start_dir = "../data/3500_legal_drafts"
# New directory for text files
output_dir = "../data/3500_legal_drafts_text"

pdfFilePath = start_dir+'/IPR Drafts/Patents/form-1.pdf'

# text = extract_text(pdfFilePath)
# with open(output_dir+'/Fees.txt', 'w') as outFile:
#     outFile.write(text)

#######################################
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
output_string = StringIO()
# with open(pdfFilePath, 'rb') as fin:
#     extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='html', codec=None)

# with open(output_dir+'/form-1-html.txt', 'w') as outFile:
#     outFile.write(output_string.getvalue())



from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0  # is used to signal extraction from all the pages
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    # with open(output_dir+'/form-1.html', 'w') as outFile:
    #     outFile.write(text)

    fp.close()
    device.close()
    retstr.close()

# Usage
# convert_pdf_to_txt(pdfFilePath)

# trying to get metadata
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

with open(pdfFilePath, 'rb') as f:
    parser = PDFParser(f)
    doc = PDFDocument(parser)
    print(doc.info)
