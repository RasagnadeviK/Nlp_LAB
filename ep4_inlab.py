from nltk.tokenize import sent_tokenize, word_tokenize
def prar(text):
    sen=sent_tokenize(text)
    nos=len(sen)
    w=word_tokenize(text)
    nw=len(w)
    paraa=text.split('\n\n')
    nparaa=len(paraa)
    return nos,nw,nparaa
text = '''Chinky is very naughty in the class. She is known for troubling her teacher.One fine day her teacher decided to give her a punishment, so she gave her set of paraa and told her to count the number of sen, w, and number of paraa that are there in the given book. Write a python program using nltk tokenizer and help her out to complete the task.'''
nos,nw,nparaa=prar(text)
print("Number of sen:",nos)
print("Number of w:",nw)
print("Number of paraa:",nparaa)