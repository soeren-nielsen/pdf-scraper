import tabula

file = "/Users/soeren_stoevring_nielsen/Google Drive/Personligt/GitHub/pdf-scraper/document.pdf"

table1 = tabula.read_pdf(file, pages=1, multiple_tables=True)
table2 = tabula.read_pdf(file, pages=2, multiple_tables=True)

table1[0]
table2[0]

print(table1[0])