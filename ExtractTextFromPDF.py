import PyPDF2
file_path=r'C:\Users\gitaa\Desktop\Data\PDFData'
#open the pdf file
pdfFileObj = open(file_path+'\\GmailAboutTheJobOpeningDataScience.pdf', 'rb')

#Read the pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#checking the number of pages in pdf
print(pdfReader.numPages)

#Creating the page object
pageObj = pdfReader.getPage(0)

#Extract text from the pages
text = pageObj.extractText()
print(text)

print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()