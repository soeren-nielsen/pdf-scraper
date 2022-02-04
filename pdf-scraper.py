from isort import file
import re
import pdfplumber
import pandas as pd
from collections import namedtuple

# invoice = namedtuple('invoice', 'varenummer, varegruppe, varenavn, antal_kg, periode, afdeling')

file = 'Salgsstatisk - Madservice Aalborg - Lions Park.pdf'

with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

#print(text)

varenavn_re = re.compile(r'^\d{3,4} [A-Å].*')
for line in text.split('\n'):
    if varenavn_re.match(line):
        print(line)