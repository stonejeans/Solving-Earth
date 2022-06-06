<div id="top"></div>

# SOLVING EARTH

A project repository that contains solutions to the Solving Earth problem. 


## Table of contents

----

- [Problem Statement](#problem-statement)
  - [Puzzle](#puzzle)
- [First Look](#first-look)
  - [Intertools](#intertools)
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
1. Build possible combinations using a value range of 0 to 9. 
2. Assign those combination values to characters. 
3. Iterate through the combinations and determine if the equation holds true. 
4. Get max value.

<br>

### Intertools:
Initial Runtime Tests:  
```
Solving Earth Max Value: 97850
Runtime: 685707.3515 ms
```

### Pandas / Numpy:
Initial Runtime Tests:
<br>
```
Solving Earth Max Value: 97850
Runtime: 66035.6451 ms
```
<br><br>
With a 10x efficiency gain over Intertools, using Pandas and Numpy is heading in the right direction.
We can obtain some useful information regarding the dtypes and memory usage of our DataFrames.
<br><br>
```
dtypes: int32(5), object(10)
memory usage: 2.0 GB
```
<br><br>

<p align="right">(<a href="#top">back to top</a>)</p>



----


## Project Approach
<br><code>se-intertools.py</code> project file demonstrates the use of the Itertools library to create permutations and list comprehensions to compile searchable lists and dictionaries. 
<br><code>se-pandas-numpy.py</code> project file demonstrates the use of Pandas to create DataFrames and Numpy to build the permutations needed to solve the problem statement equation.
<br>

<p align="right">(<a href="#top">back to top</a>)</p>



----


## Setup guide

### Prerequisites:

- [Python]()
- [Pandas]()
- [Numpy](https://numpy.org/)

<br>

### Installation:

This is a [Python]() project with dependancies through the
[pip registry]().

Before running the code, [download and install Python]().

Installation is done using the
[`pip install` command]():

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

- Website - [Coming Soon]()
- Developer - [Shaun Bristow]()

