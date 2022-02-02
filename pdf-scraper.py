from numpy import require
import requests
import pdfplumber
import pandas as pd
from collections import namedtuple

faktura = namedtuple('faktura', 'periode, varenummer, varegruppe, antal_kg, afdeling')

def download_file(url):
    local_filename = url.splut('/')[-1]

    with requests.get(url) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)
        
    return local_filename

ap_url = 'https://drive.google.com/file/d/1ME2UbVSgn6A5KWiSwvoraBwRVVFFLvBh/view?usp=sharing'

ap = download_file(ap_url)

with pdfplumber.open(ap) as pdf:
    page = pdf.pages(0)
    text = page.extract_text()

print(text)