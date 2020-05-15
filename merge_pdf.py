import contextlib
import PyPDF2

pdf_files_list = ['C:\\repositorio\\teste_pdf\\pdf_split\\fatura_71722865_detalhada_0.pdf', 'C:\\repositorio\\teste_pdf\\pdf_split\\fatura_71722865_detalhada_1.pdf', 'C:\\repositorio\\teste_pdf\\pdf_split\\fatura_71722865_detalhada_2.pdf', 'C:\\repositorio\\teste_pdf\\pdf_split\\fatura_71722865_detalhada_346.pdf']

with contextlib.ExitStack() as stack:
    pdf_merger = PyPDF2.PdfFileMerger()
    files = [stack.enter_context(open(pdf, 'rb')) for pdf in pdf_files_list]
    for f in files:
        pdf_merger.append(f)
    with open('Python_Tutorial_merged_contextlib.pdf', 'wb') as f:
        pdf_merger.write(f)