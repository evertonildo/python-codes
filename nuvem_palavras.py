#pip install python-docs
#pip install wordcloud
# Importar os módulos necessários
import docx
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Abrir o documento
document = docx.Document('docx-files\Presidência da República.docx')

# Junte todos os parágrafos em um único string
text = ""
for paragraph in document.paragraphs:
    text += paragraph.text + " "

# Criar a nuvem de palavras
wordcloud = WordCloud().generate(text)

# Mostrar a nuvem de palavras
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
#plt.figure(figsize=(150, 100))
plt.axis("off")
plt.show()