import PyPDF2

from datetime import datetime

ini = datetime.now()

path_split = "C:\\repositorio\\teste_pdf\\pdf_split\\"
with open('C:\\repositorio\\teste_pdf\\fatura_71722865_detalhada.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for i in range(pdf_reader.numPages):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(i))
        output_file_name = f'fatura_71722865_detalhada_{i}.pdf'
        path_final = path_split + output_file_name
        with open(path_final, 'wb') as output_file:
            pdf_writer.write(output_file)

fim = datetime.now()
print(fim - ini)