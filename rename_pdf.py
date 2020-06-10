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


def identify_name_pdf(path_file, operator_code):

    if operator_code == 'TIM':
        operator = 'TIM'
        reference = '(REF: [A-Z]{3}\/[0-9]{2})'
        account = '(CLIENTE: [0-9]{1}.[0-9]{7})'

    if operator_code == 'CLARO':
        operator = 'Claro'
        reference = '(Data de Emissão: [0-9-]{2}\/[0-9]{2}\/2020)'
        account = '(Nº da Conta: [0-9]{9})'


    with open(path_file, 'rb') as fp:
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

        if operator_code == 'TIM':
            account = account.replace('.', '')
            account = account.replace('CLIENTE: ', '')

            reference = reference.replace('REF: ', '')
            reference =  dateparser.parse(reference, settings={'TIMEZONE': 'America/Sao_Paulo'})
            reference = datetime.strftime(reference, "%Y%m")
        
        if operator_code == 'CLARO':
            operator = operator.upper()

            reference = reference.replace('Data de Emissão: ', '')
            reference = reference[3:10]
            reference =  dateparser.parse(reference, settings={'TIMEZONE': 'America/Sao_Paulo'})           
            reference = datetime.strftime(reference, "%Y%m")

            account = account.replace('Nº da Conta: ','')

        path_file = "C:\\repositorio\\teste_pdf\\pdf_split\\"
        # path_file = 'C:\\Users\\BRCAP-BI01\\Desktop\\Claro Car\\'


        new_name_pdf = path_file + str(reference) + '-' + operator + '-' + account + '.pdf'
        print(new_name_pdf)
        return new_name_pdf

# if __name__ == "__main__":
#     path = 'C:\\Users\\BRCAP-BI01\\Desktop\\Claro Car\\bf.blim_307024353_002_M1_PS.TAMB[1].pdf'
#     new_name_pdf = identify_name_pdf(path, 'CLARO')
#     os.rename(path, new_name_pdf)