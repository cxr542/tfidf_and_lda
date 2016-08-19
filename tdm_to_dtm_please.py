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
"""stopwords.words('english').append("it")
stopwords.words('english').append("may")
stopwords.words('english').append("you")
stopwords.words('english').append("your")
stopwords.words('english').append("in")
stopwords.words('english').append("to")
stopwords.words('english').append("us")
stopwords.words('english').append("use")
stopwords.words('english').append("keep")
"""
StopWords = set(stopwords.words("english"))
    # add custom words
StopWords.update(('and', 'may', 'a', 'use', 'us','so', 'your', 'this', 'when', 'it', 'many', 'can', 'set', 'cant',
                            'to', 'yes', 'not', 'no', 'these','keep','enough'))
docs=[]
wnl = WordNetLemmatizer()
tdm = textmining.TermDocumentMatrix()
"""str2="foods;"
a=str2.translate(None,string.punctuation)
print(a)
docs=[]
wnl = WordNetLemmatizer()
tdm = textmining.TermDocumentMatrix()
a=wnl.lemmatize("smartphones")
print(a)"""
lines = open("testdata.txt", "r").read().split('\n')
for line in lines:
    if line is None:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        break
    else:
        sentence=line.split('||')
        if (sentence.__len__() <= 2):
            # print('> item number is wrong\n')
            #wrong = 1
            #sentence.append(' ')
            #sentence.append(' ')
            continue
        sentence=sentence[1]
        sentence=sentence.lower()
        sentence=sentence.translate(None,string.punctuation)
        text = nltk.word_tokenize(sentence)

        sentence = ' '.join(a[0].lower() for a in nltk.pos_tag(text) if a[1] == 'NN')

        #stop = stopwords.words('is')
        #sentence=' '.join([w for w in sentence.split() if w not in removewordlist])
        #sentence = ' '.join([wnl.lemmatize(w) for w in sentence.split() if wnl.lemmatize(w) not in stopwords.words('english')])
        # select english stopwords

        sentence = ' '.join([wnl.lemmatize(word) for word in sentence.split() if wnl.lemmatize(word) not in StopWords])
        #sentence=' '.join(([w for w in sentence.split() if ]))
        """s = sentence.split()
        for word in s:  # iterate over word_list

            if word in stopwords.words('english') :
                s.remove(word)
            #if removewordlist in word:
               # s.remove(word)

        #s = sentence.split()
        wnl = WordNetLemmatizer()
        s=sentence.split()
        sentence = ""
        for a in s:
            #if a not in stop:
            sentence=sentence+" "+ wnl.lemmatize(a)
            """
        doc=(str(sentence))
        tdm.add_doc(doc)
        docs.append(sentence)############3
        print(sentence)

#for doc in docs:##########333
    #print(doc)###################

#tdm = textmining.TermDocumentMatrix()
#a=tdm.rows(cutoff=1)
#print (a[0])
#for doc in docs:
    #tdm.add_doc(doc)
#for row in tdm.rows(cutoff=1):
    #print(row)
#X=np.array()
print("bbbbbbbbbbbbbbbbbbbbbbbb")
#print
"""
a=tdm.write_csv("aaa.csv")

for i,a in enumerate(tdm.rows(cutoff=1)):
    if(i==0):
        vocab = tuple(a)
    #if(i==1):
       # X=np.array(a)
    #if(i>=2):
        #X=np.vstack([X,a])
    #print("count:{}".format(i),a)

#temp = list(tdm.rows(cutoff=1))
print("cccccccccccccccccccccccccccccccccccccccccccccccccc")
#vocab = tuple(temp[0])
print("ddddccdddddddddddddddddcc")
#X = np.array(temp[1:])


print("* The 'document-term' matrix")
print("type(X): {}".format(type(tdm)))
#print("shape: {}".format(tdm.shape))
print("X:", tdm, sep="\n" )
print("\n* The 'vocabulary':")
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}".format(len(vocab)))
print("vocab:", vocab, sep="\n")

model = lda.LDA(n_topics=5, n_iter=500, random_state=1)
model.fit(tdm)


topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
#print("shape: {}".format(topic_word.shape))


for n in range(4):
    sum_pr = sum(topic_word[n,:])
    print("topic: {} sum: {}".format(n, sum_pr))


n = 12
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n-{}'.format(i, ' '.join(topic_words)))
doc_topic=model.doc_topic_
"""
