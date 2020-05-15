import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import glob
from datetime import datetime
import re
import dateparser
import os

operator = 'TIM'
reference = '(REF: [A-Z]{3}\/[0-9]{2})'
account = '(CLIENTE: [0-9]{1}.[0-9]{7})'

path_file = "C:\\repositorio\\teste_pdf\\pdf_split\\fatura_71722865_detalhada_0.pdf"

fp = open(path_file, 'rb')
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
    operator_find = re.findall(operator, data)
    reference_find = re.findall(reference, data)
    account_find = re.findall(account, data)
    
operator = operator_find[0]
reference = reference_find[0]
account = account_find[0]

account = account.replace('.', '')
account = account.replace('CLIENTE: ', '')

reference = reference.replace('REF: ', '')
reference =  dateparser.parse(reference, settings={'TIMEZONE': 'America/Sao_Paulo'})
reference = datetime.strftime(reference, "%Y%m")

new_name_pdf = str(reference) + '-' + operator + '-' + account + '.pdf'


os.rename('Python_Tutorial_merged_contextlib.pdf', new_name_pdf)