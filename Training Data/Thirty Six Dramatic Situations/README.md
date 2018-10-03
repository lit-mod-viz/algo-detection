# Dataset structure for Thirty Six Dramatic Situations

In this file we describe how we structure the data available in the book and create a dataset.

## Structure of the book:
- Introduction: Irrelevant to our current needs
- Each chapter henceforth defines and gives examples of each of the thirty six dramatic situations. An example of a chapter
 stucture is illustrated below:
### Sample chapter structure
- Name of the situation
- Dynamic elements involved in the situation
- Situation is divided into groups (generally of two or three)
- Each group is further divided into different scenarios possible in that situation: **this is the data that will be useful to us**
- Each scenario has examples given from existing dramatic texts: *this does not help us because the examples are taken from popular texts, so they may not be similar enough to any text in our testing corpus.*
- Conclusions about the situation

### Relevant text files
- Situation 1: 21.txt to 25.txt
- Situation 2: 26.txt to 27.txt
- Situation 3: 28.txt to 31.txt
- Situation 4: 32.txt to 34.txt
- Situation 5: 35.txt to 37.txt
- Situation 6: 38.txt to 39.txt
- Situation 7: 40.txt to 41.txt
- Situation 8: 42.txt to 44.txt
- Situation 9: 45.txt to 46.txt
- Situation 10: 47.txt to 48.txt
- Situation 11: 49.txt to 50.txt
- Situation 12: 51.txt to 52.txt
- Situation 13: 53.txt to 56.txt
- Situation 14: 57.txt to 59.txt
- Situation 15: 60.txt to 62.txt
- Situation 16: 63.txt to 65.txt
- Situation 17: 66.txt to 69.txt
- Situation 18: 70 .txt to 72.txt
- Situation 19: 73.txt to 76.txt
- Situation 20: 77.txt to 79.txt
- Situation 21: 80.txt to 81.txt
- Situation 22: 82.txt to 83.txt
- Situation 23: 84.txt to 87.txt
- Situation 24: 88.txt to 92.txt
- Situation 25: 93.txt to 98.txt
- Situation 26: 99.txt to 103.txt
- Situation 27: 104.txt to 107.txt
- Situation 28: 108.txt to 112.txt
- Situation 29: 113.txt to 115.txt
- Situation 30: 116.txt to 117.txt
- Situation 31: 118.txt to 120.txt
- Situation 32: 121.txt to 123.txt
- Situation 33: 124.txt to 127.txt
- Situation 34: 128.txt to 129.txt
- Situation 35: 130.txt to 131.txt
- Situation 36: 132.txt to 133.txt



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
