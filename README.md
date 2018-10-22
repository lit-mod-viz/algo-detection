# Plot Genie Training and Detection

In this project we have used a dataset extracted from the Plot Genie and Plotto books to train a machine
capable of detecting the traces of historial algorithm composition.

### Our source corpus included:

- Ten Million Photoplay Plots (1919) by Wycliffe Hill 
- The Thirty-Six Dramatic Situations (1924) by Georges Polti
- Plotto (1928) by William Wallace Cook
- Plot Genie Index: General Formula (1931) by Wycliffe Hill 
- Plot Genie: Romance without Melodrama (1931)
- Plot Genie: Action-Adventure (1931)
- Plot Genie: Detective-Mystery (1933)
- Plot Genie: Short-Short Story (1934)
- Plot Genie: Detective-Mystery (1936)

### Our target corpus includes a set of articles from pulp fiction magazines written in the 1900's.

### Our testing corpus has been partitioned into two categories:

- **suspected-algo**: These are texts that we suspect have been written using our source books. For example, Adrift in the unknown by William Cook and Six gun gamble by James Olsen.
- **suspected-no-algo**: These are texts that we know have not been written paraphrased from our source. They mostly include very well known and popular texts written by reputed authors. For example, Tender Buttons by Getrude Stein.
