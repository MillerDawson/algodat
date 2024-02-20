import sys, math

def bst_sequence(linearray: list):
    updated_string = ''
    n = len(linearray)
    MIDDLE = math.floor(n/2)
    mid = linearray[MIDDLE] # calculates the middle node
    print(mid) # DEBUG --- remove this

    cur = MIDDLE - 2
    while cur >= 0 and cur <= n:
        print(linearray[cur]) # DEBUG --- change to creating new string
        cur -=2
        
    cur = 0
    while cur >=0 and cur <MIDDLE:
        print(linearray[cur]) # DEBUG --- change to creating new string
        cur+=2
        
    cur = MIDDLE+2
    while cur <n:
        print(linearray[cur]) # DEBUG --- change to creating new string
        cur +=2
        
    cur = MIDDLE+1
    while cur > MIDDLE and cur < n:
        print(linearray[cur]) # DEBUG --- change to creating new string
        cur +=2
        

numlines=int(sys.stdin.readline())
for i in range(0,numlines):
        linearray=list(map(int,sys.stdin.readline().split()))
        linearray=linearray[1:] # parses first character
        linearray.sort() # sorts the numbers

        
        print(linearray) # DEBUG ---
        bst_sequence(linearray)
        