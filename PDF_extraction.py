# This program displays metadata from pdf file

import PyPDF2 as p2

#opening the PDF so it can be read and extracted
# PDF should be in the same location as the script running. If not, use the full path to the PDF file.
PDFfile = open("dummy.pdf","rb")
pdfread = p2.PdfFileReader(PDFfile)

#Extracting a single page
x = pdfread.getPage(0)
print(x.extractText()) # Printing extracted text from PDF

#Discover is the PDF is encrypted. Returns either true or false.
print(pdfread.getIsEncrypted())
#Discover when the document was created, when, and by who.
print(pdfread.getDocumentInfo())

#Discover how many pages is in the PDF.
print(pdfread.getNumPages())

'''
# Extract entire PDF.
index = 0 # First page

# While index is less then the total number of pages in PDF
while index<pdfread.getNumPages():
    # Grab the page info
    pageinfo = pdfread.getPage(index)
    print(pageinfo.extractText())
    index = index + 1
    '''

