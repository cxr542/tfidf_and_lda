from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import string
from nltk.corpus import stopwords
#sent="Pack of 8 herb rolls to quickly and easily begin a home garden for delicious foods; includes one grass repair patch"
#sent = "Ultra Fast 3-Port USB DC Car Charger for Smartphones "
#result=open("resultfile_auto_home.txt","w")
from string import digits

s = 'abc123def456ghi789zero0'
res = s.translate(None, digits)

StopWords = set(stopwords.words("english"))
StopWords.update(('and', 'may', 'a', 'use', 'us','so', 'your', 'this', 'when', 'it', 'many', 'can', 'set', 'cant',
                            'to', 'yes', 'not', 'no', 'these','keep','enough','use','x','w','d','p','n'))

"""
port = PorterStemmer()
a=" ".join([port.stem(i) for i in sent.split()])
print(a)
"""

wnl = WordNetLemmatizer()
lines = open("testdata.txt", "r").read().split('\n')

newdata=open("newtestdata.txt","w")

for line in lines:
    sents=line.split('||')
    if (len(sents) <= 2):
            continue
    sent=sents[1]

    #tex = []
    sent = sent.lower()
    sent = sent.translate(None, string.punctuation)
    sent = sent.translate(None, digits)

    #tex = " ".join([wnl.lemmatize(i) for i in sent.split()])
    tex = ' '.join([wnl.lemmatize(word) for word in sent.split() if wnl.lemmatize(word) not in StopWords])
    #for a in nltk.pos_tag(tex.split()):
        #print(a)
    sentence = ' '

    for a in nltk.pos_tag(tex.split()):
        if a[1] == 'NN' or a[1] == 'JJ' or a[1] == 'VBN' or a[1] == 'NNS' or a[1] == 'NNP':
            sentence = sentence + a[0] + ' '
        elif a[1] == 'smartphones':
            sentence = sentence + a[0][0:len(a[0]) - 1] +' '

    newline=sents[0]+'||'+sentence+'||'+sents[2]
    newdata.write(newline+'\n')

