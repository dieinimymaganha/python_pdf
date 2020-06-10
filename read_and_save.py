import pikepdf
import os
new_pdf = pikepdf.Pdf.new()

path = 'C:\\repositorio\\teste_pdf\\'
name_pdf = '118992455_17-04-2020_3_2020_17.pdf'
path_pdf = path + name_pdf
new_pdf = 'novo.pdf'
new_path_pdf = path + new_pdf

with pikepdf.Pdf.open(path_pdf) as pdf:
    pdf.save(new_path_pdf)

os.remove(path_pdf)

os.rename(new_path_pdf,path_pdf)