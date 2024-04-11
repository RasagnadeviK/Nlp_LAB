import nltk
# Download NLTK resources (if not already downloaded)
paragraph = """Notice of a bid advertisement shall be published in at least one local newspaper
and in one trade publication at least 30 days in advance of sale. 
If applicable, the notice must identify the reservation within which the tracts to be leased are found. 
Specific descriptions of the tracts shall be available at the office of the superintendent. 
The complete text of the advertisement shall be mailed to each person listed on the appropriate agency mailing list."""

# Tokenizing sentences and finding parts of speech
sentences=nltk.sent_tokenize(paragraph)
tokenized=[]
for i in sentences:
    tokenized.append((nltk.word_tokenize(i)))
tagged=[]
for i in tokenized:
    tagged.append(nltk.pos_tag(i))
print(tagged)
'''for i in tagged:
    for j,k in i:
        print(j,"-",k)'''
