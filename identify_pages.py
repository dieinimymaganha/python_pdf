import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import glob
from datetime import datetime
import rename_pdf
import merge_pdf

def recoverfiles(pathfile):
    list_file = []
    for f in glob.glob(pathfile):
        list_file.append(f)
    return list_file

def read_pdf(list_file):
    list_due_date = []
    for f in list_file:
        with open(f, 'rb') as fp:
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
                if 'VENCIMENTO' in data or 'Fatura de Pagamento' in data or 'NOTA FISCAL DE SERVIÇOS' in data:
                    list_due_date.append(f)

    return list_due_date