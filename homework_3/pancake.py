import sys

# logic section
def pancake_sort(current_array:list) -> None:
    n = len(current_array)
    print(get_max_index(current_array)) # testing
    
    # make a loop to go through until all is sorted
    # place max index into 1st spot then 2nd until no more spots
    # add each flip to flip_sequence array
    
    # optimisation
    # testing


    
def get_max_index(current_array:list) -> int:
    """ Finds the index of the largest element """
    return current_array.index(max(current_array))

def flip_pancakes() -> None:
    """ Flips pancakes placing from range Largest to Smallest -> 1 to n """
    pass

# input section
flip_sequence = []
line = sys.stdin.readline().strip()
while line != "0":
    line_array = list(map(int, line.split()))
    pancake_sort(line_array)
    line = sys.stdin.readline().strip()
    
print(line_array)
print("0")