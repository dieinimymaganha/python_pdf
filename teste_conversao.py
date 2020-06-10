from pdfrw import PdfReader, PdfWriter


teste = open('C:\\repositorio\\teste_pdf\\file\\document-0384212176-20200525.pdf', 'rb')

x = PdfReader(teste)

y = PdfWriter()

for p in x.pages:
    y.addPage(p)

y.write('C:\\repositorio\\teste_pdf\\file\\result.pdf')