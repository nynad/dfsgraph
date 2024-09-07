# DFS is depth first search. it searches based on looking for any nodes that are "lower depth." it keeps searching for nodes that lower
# then backtracks back to the highest node. 

# how to import one function from a library :
from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edges(self,key,value):
        self.graph[key].append(value)

    def dfs_traverse(self,node,visited_set):
        visited_set.add(node) # sets cannot contain duplicate values, lists can. lists can be accessed using index numbers, sets cannot. sets are made from lists.
        print(node,end=" ") # end guarantees the text ends off the line, and your cursor stays at the same level
        for neighbour in self.graph[node]:
            if neighbour not in visited_set:
                self.dfs_traverse(neighbour,visited_set) # when calling a function within itself in a class, initialize with self
            
    def dfs(self,node):
        visited_set=set()
        self.dfs_traverse(node,visited_set)

    
graph=Graph()
graph.add_edges(0,1)
graph.add_edges(0,2)
graph.add_edges(1,2)
graph.add_edges(2,0)
graph.add_edges(2,3)

graph.dfs(2)





