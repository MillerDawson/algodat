import sys
from datetime import datetime

s,f=sys.stdin.readline().split() # splits user input
s=int(s) # int containing start value
f=int(f) # int containing end value
max_calls = 0 # running total for number of runs
start_time = datetime.now() # start time on program execution

def TNPO(n):
    running_count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        running_count += 1
    return running_count

while s <= f: 
    max_calls = max(max_calls, TNPO(s))
    s += 1

print(max_calls)
print(f"Execute time: {(datetime.now() - start_time)}") # prints execute time