from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import string
from nltk.corpus import stopwords
wnl = WordNetLemmatizer()

sent='Infrared sensor monitors driveways, doors, and mailboxes for movement and activates chiming receiver placed up to 400 ft. away and it protected our skin also improves your heads '
sent = sent.lower()
sent = sent.translate(None, string.punctuation)

tex = " ".join([wnl.lemmatize(i) for i in sent.split()])
print (tex)
for a in nltk.pos_tag(tex.split()):
    print(a)
    sentence = ' '

for a in nltk.pos_tag(tex.split()):
        if a[1] == 'NN' or a[1] == 'JJ' or a[1] == 'VBN' or a[1]=='NNS' or a[1]=='NNP':
            sentence = sentence + a[0] + ' '
        elif a[1] == 'smartphones':
            sentence = sentence + a[0][0:len(a[0]) - 1] + ' '
#print(sentence)
