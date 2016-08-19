
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

doc1="heedae is babo"
doc2="a woman is walking on the ground"
doc3="hi my name is eunsoo"
vocab=[]
StopWords = set(stopwords.words("english"))
    # add custom words
StopWords.update(('and', 'may', 'a', 'use', 'us','so', 'your', 'this', 'when', 'it', 'many', 'can', 'set', 'cant',
                            'to', 'yes', 'not', 'no', 'these','keep','enough'))
#vocab=vocab+doc1.split()
doc=["heedae is babo","a woman is walking on the ground","hi my name is eunsoo"]
doc=[]
vocab=[]
count=0
tdm = textmining.TermDocumentMatrix()

def make_matrix(num_rows,num_cols,entry_fn):
   # return [[entry_fn(i,j) for j in range(num_cols)]for i in range(num_rows)]
   return [[entry_fn(num_rows-1, j) for j in range(num_cols)]]
def is_diagonal(i,j):
    #if vocab[j] in doc[i]:
    return doc[i].split().count(vocab[j])
    #else: return 0
dtm=[]
wnl = WordNetLemmatizer()
#lines = open("auto_home.txt", "r").read().split('\n')
lines = open("testdata2.txt", "r").read().split('\n')
doc2=[]
for line in lines:
    count=count+1
    if line is None:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        break
    else:

        sentence=line.split('||')
        if (len(sentence) <= 2):
            # print('> item number is wrong\n')
            #wrong = 1
            #sentence.append(' ')
            #sentence.append(' ')
            continue
    sentence=sentence[1]
    doc2.append(sentence)
    sentence = sentence.lower()
    sentence = sentence.translate(None, string.punctuation)
    #text = nltk.word_tokenize(sentence)

    #sentence = ' '.join(a[0].lower() for a in nltk.pos_tag(text) if a[1] == 'NN')

    # stop = stopwords.words('is')
    # sentence=' '.join([w for w in sentence.split() if w not in removewordlist])
    # sentence = ' '.join([wnl.lemmatize(w) for w in sentence.split() if wnl.lemmatize(w) not in stopwords.words('english')])
    # select english stopwords

    sentence = ' '.join([wnl.lemmatize(word) for word in sentence.split() if wnl.lemmatize(word) not in StopWords])
    doc.append(sentence)
    vocab=vocab+sentence.split()
    vocab = list(set(vocab))
    dtm = dtm+ make_matrix(len(doc), len(vocab), is_diagonal)
    tdm.add_doc(sentence)

    #print (count)
#print (doc)
#for a in doc:
 #   vocab=vocab+a.split()
#vocab=list(set(vocab))
vocab = list(set(vocab))
def shape(A):
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0
    return num_rows,num_cols
#def add(entry_fn):
 #   return entry_fn(i,j)+1 for j in


def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)]for i in range(num_rows)]

def is_diagonal(i,j):
    #if vocab[j] in doc[i]:
    return doc[i].split().count(vocab[j])
    #else: return 0

print("vocab")
print (len(vocab))
#vocab=vocab+doc1.split()
dtm=make_matrix(len(doc),len(vocab),is_diagonal)
#vocab=vocab+doc2.split()
#print (vocab)
#i=make_matrix(3,3,is_diagonal)
#print shape(i)
#for a in dtm:
 #   print (a)
print (shape(dtm))
print(vocab)
print (dtm[0])

        #s = sentence.split()

#for doc in docs:##########333
    #print(doc)###################

#tdm = textmining.TermDocumentMatrix()
#a=tdm.rows(cutoff=1)
#print (a[0])
#for doc in docs:
    #tdm.add_doc(doc)
#for row in tdm.rows(cutoff=1):
    #print(row)
X=np.array(dtm)


model = lda.LDA(n_topics=11, n_iter=500, random_state=1)
model.fit(X)


topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
print("shape: {}".format(topic_word.shape))


for n in range(3):
    sum_pr = sum(topic_word[n,:])
    print("topic: {} sum: {}".format(n, sum_pr))


n = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n-{}'.format(i, ' '.join(topic_words)))
doc_topic=model.doc_topic_

for i in range(11):
    print ("{} (top topic:{})".format(doc[i],doc_topic[i].argmax()))
"""
n=[]
global n

d=[]
for b in range(18):
    sum=0
    sum2=0
    for a in dtm[b]:
        if a>0:
            sum=sum+a
    n.append(sum)
print(n[0])

#print(n[0])
#for a in n:
    #print(a)
#print(n[17])

for a in range(207):
    sum = 0
    for i in range(18):
        sum=sum+dtm[i][a]
    d.append(np.log10(19/sum))
print(d[4])
print(d[79])

def tf_idf(i):
   # print(dtm[0][4])
    tfidf={}
    #tfidf = {vocab[0]: float(dtm[0][0])/float(n[i])*d[0]}
    for j in range(207):
        tfidf[vocab[j]]=float(dtm[i][j])/float(n[i])*d[j]
    #print(type(tfidf))
    print(sorted(tfidf.iteritems(), key=itemgetter(1), reverse=True))


    #print(tfidf)

    for k in vocab:
        del tfidf[k]
    print(tfidf)
    #print(tfidf)

for i in range(18):
    print(doc2[i])
    print(doc[i])
    tf_idf(i)
    print('\n')
#print(doc[0])
"""
"""tf=[]
    tf1=[]
    idf=[]
    tf_idf=[]
    for i in range(18):
        tf1=[]
        for a in dtm[i]:
            #if n[i]==0:
                #tf1.append(0)
           # else:
            #print (a)
            if a>0:
                tf1.append(float(a/6))
            else:
                tf1.append(0)
        tf.append(tf1)
    for j in range(18):
        idf.append(np.log10(19/d[j]))
   # print(tf[0])
   # print(idf[0])
    for a in dtm[0]:
        for i in range(81):
            print(vocab[i],(tf[0][i]*idf[i]))
          #  tf_idf.append((vocab[i],(tf[0][i]*idf[i])))
    #print(tf_idf[0])"""

"""for i,a in enumerate(tdm.rows(cutoff=1)):
    if i==0:
        print(a)
    elif i==1:
        print(a)
        print(a.)

    else:
        print("ggg")
        break

#print(tdm.rows(cutoff=1))
"""