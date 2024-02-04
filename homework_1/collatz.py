import sys
from datetime import datetime

def TNPO(s, data_dict): # function takes in the s - the running start value
    if s not in data_dict: # checks if s is already in data dictionary
        if s % 2 == 0: # checks if s is even and adds s to data dictionary
            data_dict[s] = 1 + TNPO(s / 2, data_dict) 
        else: # else s is odd and then adds it to the dictionary
            data_dict[s] = 1 + TNPO(3 * s + 1, data_dict)
            
    return data_dict[s] # returns updated dictionary used in memorisation

def main():
    s,f=sys.stdin.readline().split() # splits user input
    start_time = datetime.now() # start time on program execution
    s=int(s) # int containing start value
    f=int(f) # int containing end value
    max_calls = 0 # running total for max amount of recursive calls
    data_dict = {1: 1} # data dictionary used in memorisation, to keep track of numbers called

    while s != f: # while loop to continue calling until the start number is equal to the end num
        max_calls = max(max_calls, TNPO(s, data_dict))
        s += 1 # increments s

    print(max_calls)
    print(f"Execute time: {(datetime.now() - start_time)}") # prints execute time

if __name__ == '__main__':
    main()