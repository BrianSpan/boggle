# Boggle Demonstration

### Part of a portfolio of Python Projects developed by Brian Spangler.

Demonstration of understanding of Python, data structures (list and dictionary), recursion, and Depth-First Search algorithm

- Creates a random 4x4 Boggle board (grid)
- Trim a list of words down to only those whose letters are in the grid
- Search using DFS to find any words in the grid
- Display the words found and the scores based on Boggle's scoring system

### Relevant excerpts of Hasbro's Boggle rules:
> "... words of three or more letters. Words are formed from letters that adjoin in sequence horizontally,
> vertically or diagonally in any direction. No letter may be used
> more than once within a single word..."
>
> Players score their remaining words as follows: 
> | NO OF LETTERS| 3 | 4 | 5 | 6 | 7 | 8 or more
> |--------------|---|----|-----|----|------|----------
> | POINTS| 1 |   1 |   2 |   3 |   5 |   11

### Features:
Can specify an initial list of words  
Algorithm eliminates reusing cubes (backtracking)

### Requirements:
Python 3.7+

### Sample output:
> Scrambling cubes...  
> Extracting dictionary...  
> Narrowed down to 5009 possible words  
>
> Current board:
> 
> L A E S  
> A U R U  
> L T A H  
> H H O Y   
>
> Found 164 words:  
> AARU, AHOY, AHURA,  ...
>
> |LENGTH| COUNT| POINTS| SCORE|
> |-|-|-|-|
> |  4:|   86|  X   1|  =  86|
> |  5:|   58|  X   2|  = 116|
> |  6:|   19|  X   3|  =  57|
> |  7:|    1|  X   5|  =   5|
> |    |   | TOTAL| ===== 264|


### Acknowledgements
Boggle is a copyright of Hasbro

Word list words_alpha.txt is from https://github.com/dwyl/english-words
