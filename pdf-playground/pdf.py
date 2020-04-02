import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for page in range(template.getNumPages()):
    new_page = template.getPage(page)
    new_page.mergePage(watermark.getPage(0))
    output.addPage(new_page)

with open('super-wtr.pdf', 'wb') as file:
    output.write(file)
