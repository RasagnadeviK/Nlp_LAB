import nltk
sentence="The little mouse ate the fresh cheese"
rule=r"NP:{<DT>?<JJ>*<NN>}"
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged=nltk.pos_tag(tokens)
print(tagged)
parser=nltk.chunk.RegexpParser(rule)
print(parser)
tree=parser.parse(tagged)
tree.draw()

