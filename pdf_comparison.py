import PyPDF2

def compare_pdfs(file1, file2):
    pdf1 = PyPDF2.PdfReader(open(file1,'rb'))
    pdf2 = PyPDF2.PdfReader(open(file2,'rb'))

    pages1 = len(pdf1.pages)
    pages2 = len(pdf2.pages)

    if pages1 != pages2 :
        return False

    for i in range(pages1):
        page1 = pdf1.getPage(i)
        page2 = pdf2.getPage(i)

        if page1.extract_text() != page2.extract_text():
            return False

    return True

if __name__ == '__main__':
    file1 = 'pdf1.pdf'
    file2 = 'pdf2.pdf'

    if compare_pdfs(file1,file2):
        print("Identical PDFs")
    else:
        print("Different PDFs")


