#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An example of getting titles and vocab for lda using textmine package.

-- adapted from: http://www.christianpeccei.com/textmining/

"""
from __future__ import print_function

import numpy as np
import textmining

# Create some very short sample documents
doc1 = 'John Bob brothers.'
doc2 = 'John went store. store closed.'
doc3 = 'Bob went store.'


tdm = textmining.TermDocumentMatrix()

# Add the documents
tdm.add_doc(doc1)
tdm.add_doc(doc2)
tdm.add_doc(doc3)
#print("shape: {}".format(tdm.shape))
for row in tdm.rows(cutoff=1):
    print(row)
# create a temp variable with doc-term info
temp = list(tdm.rows(cutoff=1))

# get the vocab from first row
vocab = tuple(temp[0])

# get document-term matrix from remaining rows
X = np.array(temp[1:])
np.savetxt('np.csv',X,fmt='%.f',delimiter=',')
##
## print out info, as in blog post with a little extra info
##
## post: http://bit.ly/1bxob2E
##
print("\n** Output produced by the textmining package...")

# document-term matrix
print("* The 'document-term' matrix")
print("type(X): {}".format(type(X)))
print("shape: {}".format(X.shape))
print("X:", X, sep="\n" )

# the vocab
print("\n* The 'vocabulary':")
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}".format(len(vocab)))
print("vocab:", vocab, sep="\n")
print("-- These are the 12 words in the vocabulary\n"
      "-- Often common 'stop' words, like 'and', 'the', 'to', etc are\n"
      "   filtered out -before- creating the document-term matrix and vocab")
for row in X:
    print(row)
