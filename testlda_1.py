#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
ex002.py -- An example of LDA in Python.
"""

#from __future__ import division, print_function
from copy import deepcopy

import textmining
import numpy as np
import lda
import lda.datasets

import textmining

from numpy import ceil


def termdocumentmatrix_example():
    # Create some very short sample documents
    doc1 = 'John and Bob are brothers.'
    doc2 = 'John went to the store. The store was closed.'
    doc3 = 'Bob went to the store too.'
    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    # Add the documents
    tdm.add_doc(doc1)
    tdm.add_doc(doc2)
    tdm.add_doc(doc3)
    tdm.write_csv('matrix.csv', cutoff=1)
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.
    #tdm.write_csv('matrix.csv', cutoff=1)
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
    print type(tdm)
    tdm2=deepcopy(tdm)
   # print type(T(tdm))
    for row in tdm.rows(cutoff=1):
        print row

termdocumentmatrix_example()
"""
# document-term matrix
X = lda.datasets.load_reuters()
print("type(X): {}".format(type(X)))
print("shape: {}\n".format(X.shape))

# the vocab
vocab = lda.datasets.load_reuters_vocab()
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}\n".format(len(vocab)))

# titles for each story
titles = lda.datasets.load_reuters_titles()
print("type(titles): {}".format(type(titles)))
print("len(titles): {}\n".format(len(titles)))



doc_id = 0
word_id = 3117

print("doc id: {} word id: {}".format(doc_id, word_id))

print("-- count: {}".format(X[doc_id, word_id]))


print("-- word : {}".format(vocab[word_id]))
print("-- doc  : {}".format(titles[doc_id]))


model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(X)


topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
print("shape: {}".format(topic_word.shape))


for n in range(5):
    sum_pr = sum(topic_word[n,:])
    print("topic: {} sum: {}".format(n, sum_pr))


n = 5
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))
doc_topic=model.doc_topic_
for i in range(100):
    print ("{} (top topic:{})".format(titles[i],doc_topic[i].argmax()))
    """