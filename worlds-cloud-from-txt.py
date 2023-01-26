from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#print(stopwords.words('portuguese'))

# Abre o arquivo de texto e lê o conteúdo
text = open('txt-files/presidencia.txt').read()

# Cria uma lista de palavras para excluir da nuvem de palavras
#stopwords = set(STOPWORDS)
#print('stopwords', stopwords)
stopwords = nltk.corpus.stopwords.words('portuguese') #open('txt-files/worldstops.txt').read() #set(open('txt-files/worldstops.txt').read())
#print('stopwords', stopwords)
# Gera a nuvem de palavras
wordcloud = WordCloud(stopwords=stopwords).generate(text)

# Mostra a nuvem de palavras
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
