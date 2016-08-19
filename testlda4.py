from __future__ import print_function
import string
import numpy as np
import textmining
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import lda
from nltk.corpus import wordnet
import nltk
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
#print (shape(dtm))

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
print(X.shape)

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
    print ("{} (top topic:{})".format(i,doc_topic[i].argmax()))