import os
import sys
from PyPDF2 import PdfFileReader
import re




path = sys.argv[1]
pdf = PdfFileReader(open(path),'rb')
pages = pdf.getNumPages()

print('total pages in file {} is {}'.format(path, pages))