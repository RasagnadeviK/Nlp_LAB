import nltk
from nltk.tokenize import word_tokenize
text = "There is a change in a medium."
tokens = nltk.word_tokenize(text)
print("Parts of Speech: ",nltk.pos_tag(tokens))
prep = ['a','an','the','in','and','is','are','for','of','was','were']
rd=[]
for i in tokens:
    if i not in prep:
        rd.append([i])
print("Before: ",tokens)
print("After: ",rd)

