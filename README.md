# Plot Genie Training and Detection

In this project we have used a dataset extracted from the Plot Genie and Plotto books to try and predict if a given text corpus has been written using Plot Genies or not.

#### Our source corpus included:

- Ten Million Photoplay Plots (1919) by Wycliffe Hill 
- The Thirty-Six Dramatic Situations (1924) by Georges Polti
- Plotto (1928) by William Wallace Cook
- Plot Genie Index: General Formula (1931) by Wycliffe Hill 
- Plot Genie: Romance without Melodrama (1931)
- Plot Genie: Action-Adventure (1931)
- Plot Genie: Detective-Mystery (1933)
- Plot Genie: Short-Short Story (1934)
- Plot Genie: Detective-Mystery (1936)

#### Our target corpus includes a set of articles from pulp fiction magazines written in the 1900's.

#### Our testing corpus has been partitioned into two categories:

- **suspected-algo**: These are texts that we suspect have been written using our source books. For example, Adrift in the unknown by William Cook and Six gun gamble by James Olsen.
- **suspected-no-algo**: These are texts that we know have not been written paraphrased from our source. They mostly include very well known and popular texts written by reputed authors. For example, Tender Buttons by Getrude Stein.

#### Prediction:

We have trained both a word2vec model (baseline) and an LDA model on our entire corpus, and used that trained model to get a similarity metric with a given corpus, using which we can say if that corpus has been written using plot genies or not. 


*Note*: Training both models take a very long time, because of which they were trained on an AWS server, the code for which is in the .py files in both the word2vec and LDA folders.