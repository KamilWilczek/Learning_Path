import PyPDF4
import os

os.chdir('D:\\Kursy\\Automate the boring stuff\\temp')
# pdfFile = open('meetingminutes.pdf', 'rb')
# reader = PyPDF4.PdfFileReader(pdfFile)
#
# print(reader.numPages)
#
# page = reader.getPage(0)
# print(page.extractText())
#
# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF4.PdfFileReader(pdf1File)
reader2 = PyPDF4.PdfFileReader(pdf2File)

writer = PyPDF4.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
