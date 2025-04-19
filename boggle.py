"""Create a Boggle board and create all the possible words from it"""

#both functions are used in scrambling the cubes into the grid
from random import randrange, sample

#Choose which initial list to get words from
filein="words_alpha.txt" #from https://github.com/dwyl/english-words
#filein="words_alpha1.txt" #modified to not include abbreviations like HDQRS or FLDXT
#filein="shorttestlist.txt" #a short list I made for testing
#filein="10k.txt" # 10 thousand most common words

#Constants:
# CUBES : The faces of the 16 cubes included
# NODES : the cubes that touch a particular cube
# POINTS: points per length of word (key=length,value=points)

#board configuration
#  0  1  2  3
#  4  5  6  7
#  8  9 10 11
# 12 13 14 15
CUBES:list[str]=["AAEEGN","ABBJOO","ACHOPS","AFFKPS",
                 "AOOTTW","CIMOTU","DEILRX","DELRVY",
                 "DISTTY","EEGHNW","EEINSU","EHRTVW",
                 "EIOSST","ELRTTY","HIMNUQ","HLNNRZ"]

NODES:list[list[int]]=[[1,4,5],      [0,2,4,5,6],          [1,5,6,7,3],          [2,6,7],
                      [0,1,5,8,9],  [0,1,2,4,8,6,9,10],   [1,2,3,5,7,9,10,11],  [2,3,6,10,11],
                      [4,5,9,12,13],[4,5,6,8,10,12,13,14],[5,6,7,9,11,13,14,15],[6,7,10,14,15],
                      [8,9,13],     [8,12,9,10,14],       [9,10,11,13,15],      [10,11,14]] 

#For each 3 and 4 letter word, 1 point
#5 letter words, 2 points, 6 letter words are 3 points, etc
#to maximum of 16 letters (maximum number of cubes
POINTS:dict={ 3:1,  4:1,   5:2,   6:3,
              7:5,  8:11,  9:11,  10:11,
             11:11, 12:11, 13:11, 14:11,
             15:11, 16:11}

###########
# FUNCTIONS
###########


def getdictionary(filein:str,boardletters:list)->list:
    #make shorter dictionary of possible words
    #remove words that have letters other than on board
    boardset=set(boardletters)
    with open("./wordlist/"+filein,"r") as f:
        words=[word
               for entry in f
               if (len(word:=clean(entry))>=3)  #minimum word length: 4
               and set(word).issubset(boardset)  #remove words that have other letters
              ]
    print("Narrowed down to "+str(len(words))+" possible words")    
    return(words)


def createboard(cubes:list)->list:
    #16 cubes, 6 faces
    #I shuffle the list twice because... well, because
    out=[cubes[i][randrange(6)]
         for i in permute(permute([*range(16)]))
        ]
    return(out)


def recurs(wrd:str,letidx:int,stack:list)->None: #we continue for all iterations
    global results
    #print(len(word),letidx)
    if len(wrd)!=letidx+1: #have we found all letters?  
        pos=NODES[stack[letidx]]
        for i in range(len(pos)): 
            if wrd[letidx+1]==board[pos[i]]:
                stack[letidx+1]=pos[i]
                recurs(wrd,letidx+1,stack)
    else:
        #we found the whole word
        #save it, unless we used the same cube twice
        #we may have several paths to make the same word
        if norepeatslst(stack): #no backtracking
            results[wrd]=results.setdefault(wrd,'')\
                         +(',' if (results[wrd]!='') else '')\
                         +str(stack)
    return()

#Helper functions


def permute(inlist:list)->list:
    #equivalent to numpy's permutation()
    #written just to avoid bringing in an external library
    return(sample(inlist,len(inlist)))


def clean(word:str) -> str:
    return(word.strip().upper())


def norepeatslst(inlist:list)-> bool:
    return(len(set(inlist))==len(inlist))


###########
# Main program
###########
#initialize
board:list[str]=['']*16
stack:list[int]=[]
results:dict[str,list]={}
scorelen:dict[int,int]={}

#############
# MAIN PROGRAM
#############
print("Scrambling cubes...")
board=createboard(CUBES)
print("Extracting dictionary...")
posswords=getdictionary(filein,board)

#see if any paths can be made
for word in posswords:
    stack=[0]*len(word)
    letter=0

    #find positions of ititial letter
    pos = [squar for squar, ltr in enumerate(board) if ltr == word[letter]]
    #fond next letter recursively
    for i in range(len(pos)):
        stack[0]=pos[i]
        recurs(word,0,stack)

#print the grid:
print("\nCurrent board:")
for i in range(0,16,4):
    print(*board[i:i+4])
    
#print the words we found
print("\nFound "+str(len(results))+" words:")
print(", ".join(sorted(list(results.keys()))))

#Final total
#calculate count of lengths
for i in results:
    scorelen[len(i)]=scorelen.setdefault(len(i),0)+1   
scorelen=dict(sorted(scorelen.items()))

total=0
print('\nLENGTH COUNT POINTS SCORE')
for length,count in scorelen.items():
    total+=(subtotal:=count*POINTS[length])
    print(f"{length:4}: {count:4}  X{POINTS[length]:4}  ={subtotal:4}")
print(f"         TOTAL ===== {total:3}")
