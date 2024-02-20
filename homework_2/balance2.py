import sys, math

def bst_sequence(linearray: list):
    if not linearray: # base case for recursion 
        return []
    MIDDLE = math.floor(len(linearray)/2) # MIDDLE is used as a constant for recursion below
    
    return [linearray[MIDDLE]] + bst_sequence(linearray[:MIDDLE]) + bst_sequence(linearray[MIDDLE+1:]) # recursive calling
    
numlines=int(sys.stdin.readline())
for i in range(0,numlines):
    linearray=list(map(int,sys.stdin.readline().split()))
    linearray=linearray[1:] # parses first character
    linearray.sort() # sorts the numbers
    print(' '.join(map(str, bst_sequence(linearray)))) # calls function to get the sequence then prints