import pyttsx3
import PyPDF2

book = open('Python.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.pages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.read()
text = page.extractText()
speaker.say(text)
speaker.runAndWait()