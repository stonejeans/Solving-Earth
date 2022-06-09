<div id="top"></div>

# SOLVING EARTH

A project repository that contains solutions to the Solving Earth problem. 


## Table of contents

----

- [Problem Statement](#problem-statement)
  - [Puzzle](#puzzle)
- [First Look](#first-look)
  - [Itertools](#itertools)
  - [Pandas / Numpy](#pandas-numpy)
- [Project Approach](#project-approach)
  - [Built with](#built-with)
- [Setup Guide](#setup-guide)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Author](#author)

----


## Problem Statement:

Write a computer program that will find and output all the possible combinations or solutions to the puzzle. One solution is provided, you need to find how many correct solutions exist. Your code should output all the permutations where the equation is solved correctly. The faster the code executes the better it will be. A good benchmark is to try and get your code to complete in less than 50ms.
 

### Puzzle:

There are 10 unique characters in the below puzzle, assign a unique number from 0 to 9 to each character, so that the equation holds true. An example of one positive solution is on the right:


| Solving Earth | Sample Solution  | 
| ------------- | ---------------- |
| NORTH +       | 56184            |
| EAST  +       | 7308             |
| SOUTH +       | 06984            |
| WEST  =       | 2708             |
| EARTH         | 73184            |


<p align="right">(<a href="#top">back to top</a>)</p>



## First Look:
The problem statement is solved through addressing 4 sub-problems. 
1. Calculate all possible unique combinations using a value range of 0 to 9. 
2. Assign those combination values to characters. 
3. Iterate through the combinations and determine if the equation holds true. 
4. Get max value.

<br>

### Itertools:
Initial Runtime Tests:  
```
Solving Earth Solutions: 24
Runtime: 685707.3515 ms
```

### Pandas / Numpy:
Initial Runtime Tests:
<br>
```
Solving Earth Solutions: 24
Runtime: 66035.6451 ms
```

### Pandas / Numpy (Optimised):
Initial Runtime Tests:
<br>
```
Solving Earth Solutions: 24
Runtime: 15680.4082 ms
```

### Pandas / Numpy (Refactored):
Initial Runtime Tests:
<br>
```
Solving Earth Solutions: 24
Runtime: 4485.6159 ms
```

### Pandas / Numpy (*Cheat Mode):
Initial Runtime Tests:
<br>
```
Solving Earth Solutions: 24
Runtime: 1140.7ms
```
<br><br>
With over 153x efficiency gains over Itertools, using the Pandas and Numpy library is a step in the right direction towards to 50ms benchmark.
We can obtain some useful information regarding the dtypes and memory usage of our DataFrames.
<br><br>
```
dtypes: object(5)
memory usage: 2.0 GB
```
<br><br>

<p align="right">(<a href="#top">back to top</a>)</p>



----


## Project Approach
<br><code>se-intertools.py</code> demonstrates the use of the Itertools library to create permutations and list comprehensions to compile searchable lists and dictionaries.<br>
<br><code>se-pandas-numpy.py</code> demonstrates the use of Pandas to create DataFrames and Numpy to build the permutations needed to solve the problem statement equation.<br>
<br><code>se-pandas-numpy-opt.py</code> is based on the same approach as seen in <code>se-pandas-numpy.py</code>. Here we use some cleanup techniques to remove redundencies and assist with runtime efficiency gains.<br>
<br><code>se-pandas-numpy-ref.py</code> introduces enhanced clean-up of redundant values. Efficiency gains are noticed due to the reduction in the dataframe size.<br>
<br><code>se-speed-not-read.py</code> demonstrates refactoring with efficiency in mind rather than legibility. This is NOT the preferred solution, however expanding on the conditional parameters, while pushing the overhead from the pandas Dataframe to numpy array, surprising efficiency gains are noticed.<br>

<p align="right">(<a href="#top">back to top</a>)</p>



----


## Setup guide

### Prerequisites:

- [Python](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)

<br>

### Installation:

This is a [Python](https://www.python.org) project with dependancies through the
[pip registry](https://pypi.org/).

Before running the code, [download and install Python](https://www.python.org/downloads/).

Installation is done using the
[`pip install` command](https://pypi.org/):

**1. Install Pandas:**
  ```sh
  pip install pandas
  ```
**2. Install Numpy:**
  ```sh
  pip install numpy
  ```
<br>

<p align="right">(<a href="#top">back to top</a>)</p>



----


## Author
- Developer - [Shaun Bristow](https://github.com/stonejeans/)

