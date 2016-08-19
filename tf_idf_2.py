from __future__ import print_function
import numpy as np
from operator import itemgetter

import string
import numpy as np
import textmining
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
vocab=[]
homeimprovement=open("auto_home_improvement.txt","r").read()
homegarden=open("home_garden.txt","r").read()
mensfashion=open("mensfashion.txt","r").read()
electronics=open("electronics.txt","r").read()
womensfashion=open("womensfashion.txt","r").read()
babykidstoys=open("baby_kids_toys.txt","r").read()
jewelrywatches=open("jewelry_watches.txt","r").read()
healthbeauty=open("healthbeauty.txt","r").read()
sportsoutdoors=open("sports_outdoors.txt","r").read()
grocery=open("grocery.txt","r").read()
entertainment=open("entertainment.txt","r").read()

vocab=vocab+homeimprovement.split()
vocab=vocab+homegarden.split()
vocab=vocab+mensfashion.split()
vocab=vocab+electronics.split()
vocab=vocab+womensfashion.split()
vocab=vocab+babykidstoys.split()
vocab=vocab+jewelrywatches.split()
vocab=vocab+healthbeauty.split()
vocab=vocab+sportsoutdoors.split()
vocab=vocab+grocery.split()
vocab=vocab+entertainment.split()


vocab = list(set(vocab))
doc=[]
doc.append(homeimprovement)
doc.append(homegarden)
doc.append(mensfashion)
doc.append(electronics)
doc.append(womensfashion)
doc.append(babykidstoys)
doc.append(jewelrywatches)
doc.append(healthbeauty)
doc.append(sportsoutdoors)
doc.append(grocery)
doc.append(entertainment)

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
        if dtm[i][a]>0:
            sum=sum+1
   # print(sum)
    d.append(np.log10(float(doccount+1)/float(sum)))


def tf_idf(i):
    tfidf={}
    if n[i]==0:
        return
    for j in range(vocabcount):
        tfidf[vocab[j]] = float(dtm[i][j]) / float(n[i]) * d[j]

        #if dtm[i][j] <3:
           # tfidf[vocab[j]] = float( 0.0) / float(n[i]) * d[j]
       # elif dtm[i][j] >=3:
           # tfidf[vocab[j]]=float(dtm[i][j])*10.0/float(n[i])*d[j]
    new=sorted(tfidf.iteritems(), key=itemgetter(1), reverse=True)
    abc=[]
    count=0
    for i,a in enumerate(new):
        if new[i][1]>0:
           abc.append("'"+new[i][0]+"'"+",")
           count=count+1
        if count==50:
            break
    print(abc)


for i in range(11):


    tf_idf(i)
