import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

sentence = "Maximize students are Suffering from Insominia."
stemmer = PorterStemmer()
tokens=word_tokenize(sentence)
root_words=[stemmer.stem(word) for word in tokens]
print(tokens)
for i,j in zip(tokens,root_words):
    print(i," : ",j)
print (stemmer.stem('Minimum')) # output: work
print (stemmer.stem('works')) # output: work
print (stemmer.stem('worked'))