#!/usr/bin/env python
# coding: utf-8

# # Import files

# In[1]:


import gensim
from gensim.models import Word2Vec
from gensim import corpora
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import glob


# # Read all files and create training corpus

# In[2]:


files = glob.glob('../pre-processing/combined/combined-everything.txt')
list_of_tokens=[]
for file_name in files:
    file = open(file_name,'r')
    txt = file.read()
    list_of_tokens = list_of_tokens + txt.split('\n')
    
corpus = [element.split(" ") for element in list_of_tokens]


# In[3]:


training_corpus = []
for line in corpus:
    training_corpus.append([elem for elem in line if elem != ''])


# # Train the word2vec model on the corpus

# In[4]:


model = Word2Vec(training_corpus, size=50, window=3, min_count=1, workers=8, sg=1)
model.train(training_corpus, total_examples=len(training_corpus), epochs=10)


# In[5]:


model.save('word2vec_model.model')


# # Find mean similarity of  every sentence in test to source

# In[14]:


w2v_model = gensim.models.Word2Vec.load('word2vec_model.model')


# In[18]:


#open the source file, convert it in the required form
source_file = open('../pre-processing/combined/combined-source.txt','r')
source_lines = source_file.read()
source_tokens = []
source_tokens = source_tokens + source_lines.split('\n')

s_corpus = [element.split(" ") for element in source_tokens]

source_corpus = []
for line in s_corpus:
    if line != ['']: #remove any extra blank words in the list
        source_corpus.append([elem for elem in line if elem != ''])


# In[19]:


#open the test file, convert it in the required form
test_file = open('../pre-processing/combined/combined-test-suspected-algo.txt','r')
test_lines = test_file.read()
test_tokens = []
test_tokens = test_tokens + test_lines.split('\n')

t_corpus = [element.split(" ") for element in test_tokens]

test_corpus = []
for line in t_corpus:
    if line != ['']: #remove any extra blank words in the list
        test_corpus.append([elem for elem in line if elem != ''])


# In[20]:


#calculate the similarity between every sentence in the source and every sentence in the test
similarity=[]
for test_sentence in test_corpus: #iterate over every sentence in the test corpus
    similarities=[]
    for source_sentence in source_corpus: #for every sentence in the test, iterate over every sentence in the source
        similarities.append(w2v_model.wv.n_similarity(source_sentence,test_sentence))
    #out of all similarities for each sentence in the test to every sentence in the source, get the maximum one
    similarity.append(similarities)


# In[58]:


similarity


# In[59]:


mean_similarity = sum(max_similarity)/float(len(max_similarity))


# In[60]:


mean_similarity


# In[67]:


x=[]
for i in range(0,len(max_similarity)):
    x.append(i+1)


# In[68]:


y = max_similarity


# In[69]:


plt.scatter(x, y)
plt.xlabel('sentence number')
plt.ylabel('max similarity')
plt.show()


# #### Repeat the same for suspected-no-slgo and source corpus

# In[62]:


test_file_no_algo = open('../pre-processing/combined/combined-test-suspected-no-algo.txt','r')
test_lines_no_algo = test_file_no_algo.read()
test_tokens_no_algo = []
test_tokens_no_algo = test_tokens_no_algo + test_lines_no_algo.split('\n')

t_corpus_no_algo = [element.split(" ") for element in test_tokens_no_algo]

test_corpus_no_algo = []
for line in t_corpus_no_algo:
    if line != ['']:
        test_corpus_no_algo.append([elem for elem in line if elem != ''])


# In[63]:


similarity_no_algo=[]
for test_sentence in test_corpus_no_algo:
    similarities_no_algo=[]
    for source_sentence in source_corpus:
        similarities_no_algo.append(w2v_model.wv.n_similarity(source_sentence,test_sentence))
    similarity_no_algo.append(similarities_no_algo)


# In[64]:


similarity_no_algo


# In[65]:


mean_similarity_no_algo = sum(max_similarity_no_algo)/float(len(max_similarity_no_algo))


# In[66]:


mean_similarity_no_algo


# In[ ]:





# # Tests on model
# ## No need to run this chunk -just a few things I was trying

# ## Find a list of similar words for a given word

# In[62]:


w1 = "love"
model.wv.most_similar(positive=w1)


# ## Man is to woman, as king is to?

# In[63]:


model.wv.most_similar(positive=['man', 'king'], negative=['woman'], topn=1)


# ## Find a word in a list that does not belong to the same category as the other words

# In[74]:


model.wv.doesnt_match("treachery obstacle kinsman hate".split())


# ## Check the accuracy using a common file used to test the model

# In[69]:


accuracy=model.wv.accuracy("questions-words.txt")


# In[70]:


accuracy_ratio = []
category_names = []
for category in accuracy:
    if len(category['correct'])+len(category['incorrect'])>0:
        correctness = len(category['correct'])/(len(category['correct'])+len(category['incorrect']))
    else:
        correctness = 0.0
    accuracy_ratio.append(correctness)
    category_names.append(category['section'])


# In[71]:


for i in range(0,len(category_names)):
    print(category_names[i], accuracy_ratio[i])


# ## Find cosine distance between two words

# In[72]:


dist = model.wv.distance("queen","king")


# In[73]:


print(dist)


# # Visualize

# In[15]:


vocab = list(model.wv.vocab)
X = model[vocab]


# In[44]:


tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X[:200,:])


# In[47]:


df = pd.DataFrame(X_tsne, index=vocab[:200], columns=['x', 'y'])


# In[49]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])
ax.margins(-0.25,0)
for word, pos in df.iterrows():
    ax.annotate(word, pos)

