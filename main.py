import PyPDF2 as pdf
import pyttsx3 as tts

def read_pdf():
    """
        Read page 1 PDF file
    """
    
    file = open(r'./sample.pdf', mode='rb')
    pdfdoc = pdf.PdfFileReader(file)

    page_one = pdfdoc.getPage(0)
    return page_one.extract_text()


def text_to_speech():
    engine= tts.init()
    engine.say(read_pdf())
    engine.runAndWait()

text_to_speech()