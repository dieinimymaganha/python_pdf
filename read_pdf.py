import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import PyPDF2

data = 'C:\\repositorio\\teste_pdf\\fatura_71685305_detalhada.pdf_1.pdf'

fp = open(data, 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

listpage = []
list_not_page = []
increment = 0

pages = PDFPage.get_pages(fp)

for page in pages:
    interpreter.process_page(page)
    data =  retstr.getvalue()
    increment += 1
    if 'NOME DO CLIENTE' in data:
        arquivo = f'dados{increment}.txt'
        # w = open(arquivo, 'w')
        print(f'page: {increment}\n {data}')
        listpage.append(increment)
        # w.write(data + '\n')
        # print(listpage)
    else:
        list_not_page.append(increment)
        print(list_not_page)