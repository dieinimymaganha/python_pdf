import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import glob
from datetime import datetime

fp = open("C:\\repositorio\\teste_pdf\\pdf_split\\TIMGSM_0140075579_042020_4224165751_Corp_CD100.pdf", 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)
for page in pages:
    interpreter.process_page(page)
    data =  retstr.getvalue()
    print(data)