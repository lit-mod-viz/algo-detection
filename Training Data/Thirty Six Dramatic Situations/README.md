# Dataset structure for Thirty Six Dramatic Situations

In this file we describe how we structure the data available in the book and create a dataset.

## Structure of the book:
- Introduction: Irrelevant to our current needs
- Each chapter henceforth defines and gives examples of each of the thirty six dramatic situations. An example of a chapter
 stucture is illustrated below
 - Conclusion: Irrelevant to our current needs
### Sample chapter structure
- Name of the situation
- Dynamic elements involved in the situation
- Situation is divided into groups (generally of two or three)
- Each group is further divided into different scenarios possible in that situation: **this is the data that will be useful to us**
- Each scenario has examples given from existing dramatic texts: *this does not help us because the examples are taken from popular texts, so they may not be similar enough to any text in our testing corpus.*
- Conclusions about the situation


## Structure of the Dataset
The data will consist of two tables (for efficiency in storage)

### Table 1 (Situations)
- Situation #: Unique situation number for each dramatic situation **(data type: numeric, categorical: 1-36)**
- Situation Name: Name of the situation **(data type: short sentences, continuous)**
- Elements: Elements needed in a situation **(data type: list, continuos)**

### Table 2 (Scenarios)
- Example #: The number of the scenario in a particular group **(data type: numeric, continuous)**
- Scenario Text: Actual text of the scenario **(data type: short sentences, continuous)**
- Situation #: Situation in which that text belongs **(data type: numeric, categorical: 1-36)**
- Group #: Group in which that example belongs **(data type: character, categorical: A,B,C,D..)**

## Relevant text files
Situation     | File range
------------- | -------------
1             | 21-25 
2             | 26-27
3             | 28-31
4             | 32-34
5             | 35-37
6             | 38-39
7             | 40-41
8             | 42-44
9             | 45-46
10            | 47-48
11            | 49-50
12            | 51-52
13            | 53-56
14            | 57-59
15            | 60-62
16            | 63-65
17            | 66-69
18            | 70-72
19            | 73-76
20            | 77-79
21            | 80-81
22            | 82-83
23            | 84-87
24            | 88-92
25            | 93-98
26            | 99-103
27            | 104-107
28            | 108-112
29            | 113-115
30            | 116-117
31            | 118-120
32            | 121-123
33            | 124-127
34            | 128-129
35            | 130-131
36            | 132-133
