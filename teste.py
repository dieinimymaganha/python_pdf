import re

import requests
import pdfplumber
import pandas as pd
from collections import namedtuple

ap = 'C:\\repositorio\\teste_pdf\\file\\document-0384212176-20200525.pdf'

with pdfplumber.open(ap) as pdf:
    nw = pdf.pages
    for pg in pdf.pages:
        text = pg.extract_text()
        print(text)