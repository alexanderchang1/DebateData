import numpy as np
import pandas as pd
import sys
import errno
from tabula import read_pdf
import PyPDF4 as pyPdf4
from PyPDF4 import PdfFileWriter, PdfFileReader
import pdfCropMargins as pdfc
import xarray as xr
filelocation = r"C:\Users\super\PyCharmProjects\untitled\OldForumTabCards\Hopkins_Tab_Cards.pdf"
reader = pyPdf4.PdfFileReader(open(filelocation,'rb'))
pgnumber = reader.getNumPages()


from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

'''
pdf_file = PdfFileReader(open(filelocation,"rb"))
page = pdf_file.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

adjustment = 20

page.mediaBox.lowerLeft = (adjustment, adjustment)
page.mediaBox.lowerRight = (612-adjustment, adjustment)
page.mediaBox.upperLeft = (adjustment, 792-adjustment)
page.mediaBox.upperRight = (612-adjustment, 792 - adjustment)


#for example :- my custom coordinates
#page.mediaBox.lowerRight = (611, 500)
#page.mediaBox.lowerLeft = (0, 500)
#page.mediaBox.upperRight = (611, 700)
#page.mediaBox.upperLeft = (0, 700)

'''

with open(filelocation, "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("Document has %s pages." % numPages)
    adjustment = 25
    for i in range(numPages):
        page = input1.getPage(i)
        #print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        #page.trimBox.lowerLeft = (10, 10)
        #page.trimBox.upperRight = (612-10, 792-10)
        page.cropBox.lowerLeft = (adjustment, adjustment*3)
        page.cropBox.upperLeft = (adjustment, 792 - adjustment)
        page.cropBox.upperRight = (612-adjustment, 792-adjustment)
        page.cropBox.lowerRight = (612-adjustment, adjustment*3)
        #print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        output.addPage(page)


    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
        print("written")
