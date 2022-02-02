from isort import file
import pdfplumber
import pandas as pd
from collections import namedtuple

# invoice = namedtuple('invoice', 'varenummer, varegruppe, varenavn, antal_kg, periode, afdeling')

file = 'Salgsstatisk - Madservice Aalborg - Lions Park.pdf'

with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

print(text)