
import PyPDF2, pyttsx3


path = open('C:\\Users\\evert\\Dropbox\\PC (2)\\Downloads\\1984 - George Orwell.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()

speak.stop()