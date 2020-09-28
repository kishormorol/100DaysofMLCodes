#!/usr/bin/env python
# coding: utf-8

# In[491]:


import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter


# In[492]:


with open("Humayan.txt",'r',encoding = 'utf-8') as f: 
    H_text_df = f.read()
    f.close()
with open("Rabindronath.txt",'r',encoding = 'utf-8') as f: 
    R_text_df = f.read()
    f.close()
with open("Samsur.txt",'r',encoding = 'utf-8') as f: 
    S_text_df = f.read()
    f.close()


# In[493]:


H_text_df


# In[494]:


R_text_df


# In[495]:


S_text_df


# In[496]:


# Preprocessing 
#Removing Bangla puncuation, digits and white space
import string 
char_to_remove = string.punctuation


# In[497]:


R_punc_removed = [ char for char in R_text_df if char not in string.punctuation] #remove the punctution marks
S_punc_removed = [ char for char in S_text_df if char not in string.punctuation] #remove the punctution marks
H_punc_removed = [ char for char in H_text_df if char not in string.punctuation] #remove the punctution marks


# In[498]:


R_all_sentences = ''.join(R_punc_removed)
S_all_sentences = ''.join(S_punc_removed)
H_all_sentences = ''.join(H_punc_removed)


# In[499]:


digit_to_remove = "৯৮৭৬৫৪৩২১০"


# In[500]:


R_digit_removed = [ char for char in R_all_sentences if char not in digit_to_remove] #remove the digit
S_digit_removed = [ char for char in S_all_sentences if char not in digit_to_remove] #remove the punctution marks
H_digit_removed = [ char for char in H_all_sentences if char not in digit_to_remove] #remove the punctution marks


# In[501]:


R_all_sentences = ''.join(R_digit_removed)
S_all_sentences = ''.join(S_digit_removed)
H_all_sentences = ''.join(H_digit_removed)


# In[502]:


# Bi gram count


# In[503]:


R_tokens = nltk.word_tokenize(R_all_sentences)
S_tokens = nltk.word_tokenize(S_all_sentences)
H_tokens = nltk.word_tokenize(H_all_sentences)


# In[504]:


total_words_in_corpus_wc = len(R_tokens)+ len(S_tokens) + len(H_tokens)
print(total_words_in_corpus_wc)


# In[505]:


R = set(R_tokens)
S = set(S_tokens)
H = set(H_tokens)
vocabulary = len(R)+ len(S)+len(H)
print(vocabulary)


# In[506]:


Test_sentence = "কালো মুখের মধ্যে যেটা প্রথমেই চোখে পড়ে সে হচ্ছে পাখির চঞ্চুর মতো মস্ত বড়ো বাঁকা নাক ঠোঁটের সামনে পর্যন্ত ঝুঁকে পড়ে যেন পাহারা দিচ্ছে"


# In[521]:


def UniCount(test_sentence,token):
    test_tokens = nltk.word_tokenize(test_sentence)
    unicount = 0
    for word in test_tokens:
        for w in token:
            if word == w:
                unicount = unicount + 1
    return unicount/len(token)


# In[522]:


R_unicount = UniCount(Test_sentence,R_tokens)
S_unicount = UniCount(Test_sentence,S_tokens)
H_unicount = UniCount(Test_sentence,H_tokens)
print(R_unicount, S_unicount, H_unicount)


# In[523]:


def BiCount(test_sentence,token):
    test_tokens = nltk.word_tokenize(test_sentence)
    test_bgs = nltk.bigrams(test_tokens)
    test_fdist = nltk.FreqDist(test_bgs)
    author_bgs = nltk.bigrams(token)
    author_fdist = nltk.FreqDist(author_bgs)
    #print(len(author_fdist))
    bicount = 0
    for k,v in test_fdist.items():
        for ak,av in author_fdist.items():
            if k == ak:
                bicount = bicount + 1
    return bicount/len(author_fdist)


# In[524]:


R_bicount = BiCount(Test_sentence,R_tokens)
S_bicount = BiCount(Test_sentence,S_tokens)
H_bicount = BiCount(Test_sentence,H_tokens)
print(R_bicount, S_bicount, H_bicount)


# In[525]:


#Applying Naive Bayes with Bi gram count


# In[526]:


p_of_R = (R_bicount+R_unicount+1)/(total_words_in_corpus_wc+vocabulary)
p_of_S = (S_bicount+S_unicount+1)/(total_words_in_corpus_wc+vocabulary)
p_of_H = (H_bicount+H_unicount+1)/(total_words_in_corpus_wc+vocabulary)
print(p_of_R, p_of_S, p_of_H)


# In[527]:


if (p_of_R > p_of_S) and (p_of_R > p_of_H):
    print("The Author is Rabindronath Tagor")
elif (p_of_S > p_of_R) and (p_of_S > p_of_H):
    print("The Author is Samsur Rahman")
else: 
    print("The Author is Humayan Ahmed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




