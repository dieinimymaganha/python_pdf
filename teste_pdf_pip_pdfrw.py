from pdfrw import PdfWriter, PdfReader
x = PdfReader('C:\\repositorio\\teste_pdf\\document-0384212176-20200525.pdf')
y = PdfWriter()
y.addpage(x.pages[0])
y.write('C:\\repositorio\\teste_pdf\\novo2.pdf')