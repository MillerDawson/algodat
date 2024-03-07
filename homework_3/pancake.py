import sys

# logic section
def pancake_sort(array:list) -> list:
    """ Main function used in the descending pancake sort """
    flip_sequence = [] # records flip sequence
    n = len(array) # n=length of array, k = amount of sorted
    k = 0 
    sorted_array = sorted(array, reverse=True) # creates sorted array to check with
    # mainloop
    while array != sorted_array: # checks to ensure list isnt sorted
        curr_max = get_max_index(array, k, n) # gets current max index
        array = flip_pancakes(array, curr_max, k, flip_sequence)
        k+=1 # k is incremented as in correct position
    # if array is sorted
    flip_sequence.append(0)
    return flip_sequence
    
def flip_pancakes(array:list, curr_max: int, k: int, flip_sequence: list) -> list:
    """ Flips pancakes placing from range Largest to Smallest -> 1 to n """
    if curr_max != k:  # only do flips if curr_max is not already at k

        # brings flip curr_max pancake to top
        if array[-1] != array[curr_max]: # checks that largest index is not already at top 
            unchanged_portion = array[:curr_max]
            flipped_portion = array[curr_max:][::-1]
            array = unchanged_portion+flipped_portion
            
            flip_sequence.append(curr_max+1)       
        
        # flip pancake to k
        unchanged_portion = array[:k]
        flipped_portion = array[k:][::-1]
        array = unchanged_portion+flipped_portion

        flip_sequence.append(k+1)
    return array

def get_max_index(array:list, k: int, n: int) -> int:
    """ Finds the index of the largest element within range of k to n"""
    max_index = k
    for i in range(k, n): # loops through k to n
        if array[i] > array[max_index]:
            max_index = i # essentially a max function
    return max_index

    
# input section
line = sys.stdin.readline().strip()
while line != "0":
    line_array = list(map(int, line.split()))
    x = str(pancake_sort(line_array)).strip(",[]").replace(",","")
    print(x)

    line = sys.stdin.readline().strip()
print(0) # on termination as required