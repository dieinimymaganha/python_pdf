import PyPDF2
import identify_pages
import re
from datetime import datetime
import rename_pdf
import merge_pdf
import os

ini = datetime.now()

pathfile = "C:\\repositorio\\teste_pdf\\pdf_split\\*.pdf"

path_split = "C:\\repositorio\\teste_pdf\\pdf_split\\"
with open('C:\\repositorio\\teste_pdf\\TIMGSM_0140075579_042020_4224165751_Corp_CD.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for i in range(pdf_reader.numPages):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(i))
        output_file_name = f'TIMGSM_0140075579_042020_4224165751_Corp_CD{i}.pdf'
        path_final = path_split + output_file_name
        with open(path_final, 'wb') as output_file:
            pdf_writer.write(output_file)

list_file = identify_pages.recoverfiles(pathfile)
list_file = sorted(list_file, key=len)
list_due_date = identify_pages.read_pdf(list_file)

file_find_name = list_file[0]

new_name_pdf = rename_pdf.identify_name_pdf(file_find_name)

merge_pdf.merge_pdf_final(list_due_date, new_name_pdf)


for file in list_file:
    os.remove(file)

fim = datetime.now()
print(fim - ini)