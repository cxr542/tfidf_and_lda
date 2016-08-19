
from __future__ import print_function
import numpy as np
from operator import itemgetter

import string
import numpy as np
import textmining
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import lda
from nltk.corpus import wordnet
import nltk

global doccount,vocabcount

doccount=0
vocabcount=0
vocab=[]
StopWords = set(stopwords.words("english"))
StopWords.update(('and', 'may', 'a', 'use', 'us','so', 'your', 'this', 'when', 'it', 'many', 'can', 'set', 'cant',
                            'to', 'yes', 'not', 'no', 'these','keep','enough'))
doc=[]
vocab=[]
count=0
tdm = textmining.TermDocumentMatrix()

def make_matrix(num_rows,num_cols,entry_fn):
   return [[entry_fn(num_rows-1, j) for j in range(num_cols)]]
def is_diagonal(i,j):
    return doc[i].split().count(vocab[j])

dtm=[]
wnl = WordNetLemmatizer()
lines = open("entertainment.txt", "r").read().split('\n')
result=open("resultfile_auto_home.txt","w")
doc2=[]
for line in lines:
    count=count+1
    if line is None:
        break
    else:

        sentence=line.split('||')
        if (len(sentence) <= 2):

            continue
    sentence=sentence[1]
    doc2.append(sentence)
    sentence = sentence.lower()
    sentence = sentence.translate(None, string.punctuation)

    #text = nltk.word_tokenize(sentence)
    #sentence = ' '.join(a[0].lower() for a in nltk.pos_tag(text) if a[1] == 'NN')

    sentence = ' '.join([wnl.lemmatize(word) for word in sentence.split() if wnl.lemmatize(word) not in StopWords])
    doc.append(sentence)
    vocab=vocab+sentence.split()
    vocab = list(set(vocab))
    dtm = dtm+ make_matrix(len(doc), len(vocab), is_diagonal)
    tdm.add_doc(sentence)

vocab = list(set(vocab))
def shape(A):
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0

    return num_rows,num_cols

def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)]for i in range(num_rows)]

def is_diagonal(i,j):
    return doc[i].split().count(vocab[j])

dtm=make_matrix(len(doc),len(vocab),is_diagonal)

print("dtm shape")
print (shape(dtm))
doccount=shape(dtm)[0]
vocabcount=shape(dtm)[1]
#print(doccount,vocabcount)
print(vocab)
global n
n=[]


d=[]
for b in range(doccount):
    sum=0
    sum2=0
    for a in dtm[b]:
        if a>0:
            sum=sum+a
    n.append(sum)

for a in range(vocabcount):
    sum = 0
    for i in range(doccount):
        sum=sum+dtm[i][a]
    d.append(np.log10(float(doccount+1)/float(sum)))


def tf_idf(i):
    tfidf={}
    if n[i]==0:
        return
    for j in range(vocabcount):
        tfidf[vocab[j]]=float(dtm[i][j])/float(n[i])*d[j]
    new={}
    new=sorted(tfidf.iteritems(), key=itemgetter(1), reverse=True)
    print(new)
    for i,a in enumerate(new):
        if new[i][1]>0:
            result.write(str(new[i]))
    result.write('\n')
    #result.write(str(new[1]))
   # result.write(str(new[2]))

    #result.write(new)
    #result.write(print(sorted(tfidf.iteritems(), key=itemgetter(1), reverse=True)))


for i in range(doccount):
    result.write(doc2[i])
    result.write('\n')

    result.write(doc[i])
    result.write('\n')

    tf_idf(i)
    result.write('\n')
    #print(doc2[i])
    #print(doc[i])
   # tf_idf(i)
    #print('\n')
