# Dataset structure for Plot Genie - Detective Mystery

In this file we describe how we structure the data available in the book and create a dataset.

## Structure of the book:
- The Formula - General Instructions: Describes the formula to be used with the genie robot. The rest of the content is irrelevant.
The number of elements to be chosen for each categroy is provided on page number 16 - however, it is arbitary.
- Each chapter henceforth defines and gives the list for each plot requisite.
Operation 1: The Murder
  List A: Victim (180)
  List B: Locale (180)
  List C: Method of Murder (180)
  List D: Robbery - type of thing taken (10)
  List E: Forgery (10)
  List F: Destruction of property (10)
  List G: Kidnapping (10)
  
Operation 2: The Clue
  List A: List of clues (180)
  List B: List of objects (180)
  
Operation 3: Principal suspect 
  List A: List of suspects (180)

Operation 4: Method of investigation
  List A: List of methods (180)
  List B: List of methdos (180)
  
Operation 5: Suspicious situation
  List A: List of circumstances (180)
  List B: List of circumstances (180)
  List C: List of circumstances (180)
  
Operatin 6: Thrilling situation develops when
  List A: List of circumstances (180)
  
Operation 7: The solution is precipitated when
  List A: List of circumstances (180)

Operation 8: The guilty one is
  List A: List of people (180)
  
Operation 9: The motive is
  List A: List of motives (180)
  List B: List of motives (180)
  List C: List of motives (180)
  
An example of a chapter stucture is illustrated below
 
### Sample chapter structure
- Number of the operation
- Definition of the situation
- Elements involved in the situation
- Each element has a list of examples - which we will use for training. Generally it is a list of 180, but some might have fewer elements.


## Structure of the Dataset
Data can be structured in the same possible three approaches mentioned in “Index – README.md” file.

## Relevant text files
Operaition    | Text files with data
------------- | --------------------
1             | 43-59 
2             | 60-72
3             | 73-76
4             | 77-90
5             | 91-116
6             | 117-123
7             | 124-134
8             | 135-138
9             | 139-158
