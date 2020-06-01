

''' A forest is a collection of disjoint trees. In other words, we can also say that 
    forest is a collection of an acyclic graph which is not connected.'''

''' There are Three tress in the given forest or graph '''

#                        2          1           4
#                        |          |          / \
#                        |          |         /   \
#                        5          3        7     8
#                       / \         |
#                      /   \        |
#                     9     0       6
                                                         

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices                    # no. of Vertices in a Graph                           
        self.graph = defaultdict(list)              # List of Pointers to Adjacent Nodes


# ------------------ Inserting Node in a Graph -------------------
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        

# --------*-----Count number of trees in an Undirected forest or graph USing DFS !.-------*---------
    def countTrees(self):
        visited = [False] * self.vertices
        noOfTrees = 0

        for n in range(self.vertices):
            if visited[n] == False:
                self.DFSUtil(n,visited)
                noOfTrees += 1
        return noOfTrees

    def DFSUtil(self,node,visited):
        visited[node] = True
        for n in self.graph[node]:
            if visited[n] == False:
                self.DFSUtil(n,visited)


# ------------------ Testing the Graph -----------------
g = Graph(10) 
g.addEdge(2,5) 
g.addEdge(5,9)
g.addEdge(5,0)
g.addEdge(1,3)
g.addEdge(3,6)
g.addEdge(4,7)
g.addEdge(4,8) 

print("no. of forest in this Undirected Graph : ",g.countTrees())
