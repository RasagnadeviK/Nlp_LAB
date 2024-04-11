import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
para="Natural Language Processing  is a subfield of linguistics, computer science,artificial intelligence concerned with the interactions between computers and human languages."
ses=sent_tokenize(para)
top=[]
for i in ses:
    w=word_tokenize(i)
    tw=pos_tag(w)
    top.extend(tw)
for i,j in top:
    print(f"Token: {i}, POS: {j}")

