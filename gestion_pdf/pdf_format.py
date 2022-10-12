import PyPDF2

# content output (pdf file)
content_final = PyPDF2.PdfFileWriter()

# open file for reading in byte format 'rb'
file_0 = open("pdf_0.pdf", 'rb')
file_1 = open("pdf_1.pdf", 'rb')

# read pdf file
reader_presentation = PyPDF2.PdfFileReader(file_0)
reader_recap = PyPDF2.PdfFileReader(file_1)

print(f" number page of file presentation {reader_presentation.getNumPages()}")
print(f" number page of file recap {reader_recap.getNumPages()}")

# add file in pdf empty - content_final
content_final.addPage(reader_presentation.getPage(0))
# add page with the size of the file with getNumPages in for loop for add all pages
for i in range(reader_recap.getNumPages()):
    content_final.addPage(reader_recap.getPage(i))

# create file and add pdf content "wb" => write binary
file_combinator = open("combinator.pdf", "wb")
content_final.write(file_combinator)

# close all file 
file_0.close()
file_1.close()
file_combinator.close()
