from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import string
from nltk.corpus import stopwords
#sent="Pack of 8 herb rolls to quickly and easily begin a home garden for delicious foods; includes one grass repair patch"
#sent = "Ultra Fast 3-Port USB DC Car Charger for Smartphones "
#result=open("resultfile_auto_home.txt","w")
import csv
cw = csv.writer(file('testcsv.csv', 'w'))
cw.writerow(['name'])

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


for line in lines:
    sents=line.split('||')
    if (len(sents) <= 2):
            continue
    sent=sents[1]

    #tex = []
    sent = sent.lower()
    sent = sent.translate(None, string.punctuation)

    #tex = " ".join([wnl.lemmatize(i) for i in sent.split()])
    tex = ' '.join([wnl.lemmatize(word) for word in sent.split() if wnl.lemmatize(word) not in StopWords])
    #for a in nltk.pos_tag(tex.split()):
        #print(a)
    sentence = ' '

    for a in nltk.pos_tag(tex.split()):
        if a[1] == 'NN' or a[1] == 'JJ' or a[1] == 'VBN' or a[1] == 'NNS' or a[1] == 'NNP':
            sentence = sentence + a[0] + ' '
        elif a[1] == 'smartphones':
            sentence = sentence + a[0][0:len(a[0]) - 1] + ' '
    cw.writerow([str(sentence)])
    #cw.writerow([444, 555, 666])