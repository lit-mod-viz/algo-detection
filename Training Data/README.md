# Summary of the Training Corpus
Out of all PDF's available, 5 books out of 8 gave reasonably accurate results when converted from images to text using Tesseract.
Better scans and other softwares may be used to improve accuracy. 

## Format of the Data is as follows:
Each book has a folder of text files of its content. Every page of the book has an indivudual text file associated with it,
with all of its content. 
For page "n", the file would be named "n.txt".

## The list of books, in order of their accuracy, is as follows:

**1. Thirty Six Dramatic Situations** : Most accurate conversion by far, very few errors.
**2. Plot Genie Index- General Formula** : Quite accurate, but a few letters or words have not been recognised properly throughout the text.
**3. Plot Genie- Romance without Melodrama** : A lot of portions converted well, but very large errors in letter indentification, resulting in some meaningless data.
**4. Plot Genie- Detective-Mystery** : Few portions converted, but list numbers are printed seperately from list content, so might be difficult to map number to text.
**5. Plot Genie- Action-Adventure -1931** : Very few protions are accurate, and list to content mapping is not proper in this case as well.
**6. Plotto** : Scanned copy is very low resolution, so it is not able to identify any text and all files are blank. Can get better resolution of images. *Not included in the corpus for now*
**7. Ten Million Photoplay Plots** : Pages are horizontally algined and each page of the PDF has two pages of the book, so it is not able to identify any text and files have incorrectly identified content. Need to rotate and split pages.*Not included in the corpus for now*
