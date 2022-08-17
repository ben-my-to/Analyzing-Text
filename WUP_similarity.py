# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 00:43:33 2016

@author: Shilpa
"""

from nltk.corpus import wordnet as wn

def getSimi(word1, word2):
    xx = wn.synsets(word1)
    print (xx)
    
    yy = wn.synsets(word2)
    print (yy)
    
    maxi = 0
    maxiSyn =""
    for x in xx:
#        print "x:......"
#        print x.name
#        print x.lemma_names()
        for y in yy:
#            print "y....."
#        
#            print y.name
#            print y.lemma_names()
#            print x.wup_similarity(y)
            if maxi < x.wup_similarity(y):
                print (x)
                print (y)
                
                maxi = x.wup_similarity(y)
                print (maxi)
                maxiSyn = "x =" + str(x.lemma_names()) + " y ="+ str(y.lemma_names())
                print(maxiSyn)
#            print '\n'
        
    return maxi
    
print (getSimi("software","code"))