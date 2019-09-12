import numpy as np
import pandas as pd
import sys
import errno
from tabula import read_pdf
import PyPDF4 as pyPdf4
from PyPDF4 import PdfFileWriter, PdfFileReader
import pdfCropMargins as pdfc
import xarray as xr
filelocation = r"C:\Users\super\PyCharmProjects\POWExtraction\POW.pdf"
reader = pyPdf4.PdfFileReader(open(filelocation,'rb'))
pgnumber = reader.getNumPages()

df = read_pdf(filelocation, guess = False, pages = 4, area = "0,0,0,0", multiple_tables=False)
print(df)