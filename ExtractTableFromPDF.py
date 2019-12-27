import tabula
file_path=r'C:\Users\gitaa\Desktop\Data\PDFData'
# reading the table from pdf
df = tabula.read_pdf(file_path+"\\table.pdf",guess = False)
#check the data
df.head()

# when pdf contains the multiple tables
df = tabula.read_pdf(file_path+"\\table.pdf",multiple_tables=True)

# reading specific part of specific pages
tabula.read_pdf(file_path+"\\table.pdf", area=(126,149,212,462), pages=1)

# output the result into JSON
tabula.read_pdf(file_path+"\\table.pdf", output_format="json")

# out put the result into excel file
tabula.convert_into(file_path+"\\table.pdf", "table_output.xlsx", output_format="xlsx")
