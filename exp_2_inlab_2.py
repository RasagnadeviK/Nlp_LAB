import nltk
from nltk.tokenize import word_tokenize
sentence="Chinnu is the one who protect lilly"
tokens=word_tokenize(sentence)
count=len(tokens)
print(tokens)
print("Count:",count)
