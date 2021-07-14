import PyPDF2

merger = PyPDF2.PdfFileMerger()

file_names = ['cv.pdf', 'rotated.pdf']

for file in file_names:
    merger.append(file)
merger.write('combined.pdf')
