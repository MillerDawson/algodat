import sys
from datetime import datetime

def TNPO(s, data_dict): 
    if s <= 0 or not isinstance(s, int):
        raise ValueError("Input must be a positive integer")
        
    if s not in data_dict: 
        if s % 2 == 0: 
            data_dict[s] = 1 + TNPO(s // 2, data_dict) 
        else: 
            data_dict[s] = 1 + TNPO(3 * s + 1, data_dict)
            
    return data_dict[s]

def main():
    s,f = map(int, sys.stdin.readline().split()) # splits user input
    if f < s:
        raise ValueError("End value must be greater than or equal to start value")

    start_time = datetime.now() # start time on program execution
    max_calls = 0 # running total for max amount of recursive calls
    data_dict = {1: 1} # data dictionary used in memorisation, to keep track of numbers called

    while s <= f: # while loop to continue calling until the start number is equal to the end num
        try:
            max_calls = max(max_calls, TNPO(s, data_dict))
        except ValueError as e:
            print(f"Error: {e}")
            return
        s += 1 # increments s

    print(max_calls)
    print(f"Execution time: {(datetime.now() - start_time)}") # prints execute time

if __name__ == "__main__":
    main()
