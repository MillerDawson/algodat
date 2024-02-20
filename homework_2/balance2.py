import sys, math

# passes small tests, fails large scale tests

def bst_sequence(linearray: list):
    n = len(linearray) # length of linearray
    bst_str = '' # this is the string that will be used in concatenation
    MIDDLE = math.floor(n/2) # MIDDLE is used as a constant for balance calculations
    bst_str += str(linearray[MIDDLE]) + ' ' # inserts the middle node

    cur = MIDDLE - 2 # goes down the left
    while cur >= 0: 
        bst_str += str(linearray[cur]) + ' ' # adding to the bst_str
        cur -=2
    
    cur = 0 # sets to element 0 of the list
    while cur <MIDDLE: # goes backup while cur != middle
        bst_str += str(linearray[cur]) + ' ' # adding to the bst_str
        cur+=2
        
    cur = MIDDLE+2 # goes up 2's from middle
    while cur <n:
        bst_str += str(linearray[cur]) + ' ' # adding to the bst_str
        cur +=2
        
    cur = MIDDLE+1
    while cur <=n:
        bst_str += str(linearray[cur]) + ' ' # adding to the bst_str
        cur +=2
        
    return bst_str
        

numlines=int(sys.stdin.readline())
for i in range(0,numlines):
        linearray=list(map(int,sys.stdin.readline().split()))
        linearray=linearray[1:] # parses first character
        linearray.sort() # sorts the numbers

        print(bst_sequence(linearray)) # calls function to get the sequence then prints