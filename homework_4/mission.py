import sys

def can_drive(num_villages,roads):
  """You should implement this function, which takes in the number
     of villages in the problem and a set of tuples representing
     the start end end village of each road. 
     
     It returns 1 if one can drive, or -1 if one cannot drive as per the instructions."""
  pass
  
    
    

num_problems=int(sys.stdin.readline().strip())
output=""
for _ in range(num_problems):
  line=sys.stdin.readline().strip()
  num_villages,num_roads=list(map(int,line.split()))
  roads=set()
  for _ in range(num_roads):
    roads.add(tuple(map(int,sys.stdin.readline().strip().split())))
  print(can_drive(num_villages,roads))