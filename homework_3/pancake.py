import sys

# logic section
def pancake_sort(array:list) -> list:
    flip_sequence = []
    n = len(array) # k = amount of sorted, n=length of array
    k = 0 

    # print(f"Initial Array {array}")

    sorted_array = sorted(array, reverse=True) # doesnt have to repeat the sort function
    
    # mainloop
    while array != sorted_array: # slightly more efficient incase list is sorted after 1 flip
        curr_max = get_max_index(array, k, n) # gets current max index
        # print(f"CURRENTMAX {curr_max}")
        array = flip_pancakes(array, curr_max, k, n, flip_sequence)
        # print(f"ARRAY {array}")
        k+=1 # k is incremented as in correct position
        
    # if array is sorted
    flip_sequence.append(0)
    return flip_sequence
    


def flip_pancakes(array:list, curr_max: int, k: int, n: int, flip_sequence: list) -> list:
    """ Flips pancakes placing from range Largest to Smallest -> 1 to n """
    if curr_max != k:  # only do flips if curr_max is not already at k

        # brings flip curr_max pancake to top
        if array[-1] != array[curr_max]: # checks that largest index is not already at top 
            # array[:curr_max+1] = reversed(array[:curr_max+1])

            unchanged_portion = array[:curr_max]
            flipped_portion = array[curr_max:][::-1]
            array = unchanged_portion+flipped_portion
            
            flip_sequence.append(curr_max+1)
            #print("largest is not at the last index")
            #print(f"Flip sequence: {flip_sequence}")
            #print(f"After Flip of largest to the top {array}")
        
        
        # flip pancake to k
        # array = array[k:][::-1] + array[:k]
        unchanged_portion = array[:k]
        flipped_portion = array[k:][::-1]
        array = unchanged_portion+flipped_portion

        flip_sequence.append(k+1)
        
        #print(f"Flip sequence: {flip_sequence}")
        #print(f"After Flip {array}")
    
    return array

def get_max_index(array:list, k: int, n: int) -> int:
    """ Finds the index of the largest element within range of k to n"""
    max_index = k
    for i in range(k, n): # loops through k to n
        # print(f"{i}")
        # print(f"ARRAY INDEX I {array[i]}")
        if array[i] > array[max_index]:
            max_index = i # essentially a max function
            # print(max_index)
    # print(f"Current Max Index:  {max_index}")
    return max_index

    
# input section
line = sys.stdin.readline().strip()
while line != "0":
    line_array = list(map(int, line.split()))
    #print(line_array)
    x = str(pancake_sort(line_array)).strip(",[]").replace(",","")
    print(x)

    line = sys.stdin.readline().strip()
print(0)