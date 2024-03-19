import sys

# https://www.geeksforgeeks.org/eulerian-path-and-circuit/ - Reference Used Throughout

# ===== Logic Section =====
def is_connected(graph, curr, visited):
  visited[curr] = True # sets current vertex to visited
  
  # recursively for all vertex adjacent to this to check if eulerian cycle
  for vertex in graph[curr]:
    if not visited[vertex]:
      is_connected(graph, vertex, visited)

def can_drive(num_villages, roads):
  visited = [False] * num_villages # initialise visited
  graph = {i: set() for i in range(num_villages)} # initialise graph
  
  # sets graph with appropriate start/end roads
  for (start_road, end_road) in roads:
    graph[start_road].add(end_road)
    graph[end_road].add(start_road)
  
  # check if all vertices have been visited
  no_vertex = next((village for village, val in enumerate(graph.values()) if val), None)
  
  if no_vertex is None:
    return 1 # graph is a eulerian cycle
  
  is_connected(graph, no_vertex, visited)
  
  # checks if graph is connected
  for i in range(num_villages):
    if graph[i] and not visited[i]:
      return -1 
  
  # check if graph is eulerian cycle
  for i in graph.values():
    if len(i) % 2 != 0: # ensures each vertex of graph has even number degrees
      return -1 
    
  return 1 # graph meets all requirements is traversible with eulerian cycle present
  
    
# ===== User Section =====
num_problems=int(sys.stdin.readline().strip())
for _ in range(num_problems):
  line=sys.stdin.readline().strip()
  num_villages,num_roads=map(int,line.split())
  roads=set()
  for _ in range(num_roads):
    roads.add(tuple(map(int,sys.stdin.readline().strip().split())))
  print(can_drive(num_villages,roads))