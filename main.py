import PyPDF2 as pdf

def readPDF():
    """
        Read page 1 PDF file
    """
    
    file = open(r'./sample.pdf', mode='rb')
    pdfdoc = pdf.PdfFileReader(file)

    page_one = pdfdoc.getPage(0)
    return page_one.extract_text()