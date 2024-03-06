import sys

# logic section
def pancake_sort(array:list) -> None:
    n = len(array) # k = amount of sorted, n=length of array
    k = 0 

    sorted_array = sorted(array) # doesnt have to repeat the sort function
    print(f"UNSORTED: {array}\nSORTED: {sorted_array}\n\n")  # -- test
    
    # mainloop
    while array != sorted_array: # slightly more efficient incase list is sorted after 1 flip
        curr_max = get_max_index(array, k, n)
        print(curr_max)
        break
    
    # if array is sorted
    print("0")
    return
    
    # optimisation
    # testing


    
def get_max_index(array:list, k: int, n: int) -> int:
    """ Finds the index of the largest element within range of k """
    running_max = 0 # initialise running_max
    for i in range(k, n): # loops through k to n
        if array[i] > running_max:
            running_max = array[i] # essentially a max function
            
    return array.index(running_max)
    
    #  return current_array.index(max(current_array))

# input section
flip_sequence = []
line = sys.stdin.readline().strip()
while line != "0":
    line_array = list(map(int, line.split()))
    pancake_sort(line_array)
    line = sys.stdin.readline().strip()
    
print(line_array)
