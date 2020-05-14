import PyPDF2

import time

inicio = time.time()


with open('fatura_71685305_detalhada.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for i in range(pdf_reader.numPages):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(i))
        output_file_name = f'fatura_71685305_detalhada.pdf_{i}.pdf'
        with open(output_file_name, 'wb') as output_file:
            pdf_writer.write(output_file)

fim = time.time()
print(fim - inicio)