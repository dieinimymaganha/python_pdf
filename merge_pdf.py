import contextlib
import PyPDF2


def merge_pdf_final(pdf_files_list, new_name_pdf):
     with contextlib.ExitStack() as stack:
        pdf_merger = PyPDF2.PdfFileMerger()
        files = [stack.enter_context(open(pdf, 'rb')) for pdf in pdf_files_list]
        for f in files:
            pdf_merger.append(f)
        with open(new_name_pdf, 'wb') as f:
            pdf_merger.write(f)