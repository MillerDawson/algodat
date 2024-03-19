import sys

def is_connected(graph, vertex, visited):
  pass

def can_drive(num_villages,roads):
  # initialise visited
  visited = [False] * num_villages
  
  # creates empty sets for each village
  graph = {i: set() for i in range(num_villages)}
  
  
  for (start_road, end_road) in roads:
    graph[start_road].add(end_road)
    graph[end_road].add(start_road)
  
  # check if all vertices have been visited
  
  # check if graph is eulerian cycle
  for ver in graph.values():
    if len(ver) &2 != 0: # ensures each vertex of graph has even number degrees
      return -1 

  
    
# ===== User Section =====
num_problems=int(sys.stdin.readline().strip())
for _ in range(num_problems):
  line=sys.stdin.readline().strip()
  num_villages,num_roads=list(map(int,line.split()))
  roads=set()
  for _ in range(num_roads):
    roads.add(tuple(map(int,sys.stdin.readline().strip().split())))
  print(can_drive(num_villages,roads))