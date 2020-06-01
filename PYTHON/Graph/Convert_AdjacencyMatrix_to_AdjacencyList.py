

from collections import defaultdict

class Graph:

    def convert(self,temp):
        adjList = defaultdict(list)
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] == 1:
                    adjList[i].append(j)
        
        return adjList


# ------------------ Testing the Graph conversion -----------------
g = Graph()
a =[[0, 0, 1], [0, 0, 1], [1, 1, 0]] # adjacency matrix 
AdjList = g.convert(a)
for i in AdjList:
    print(i, end=" ")
    for j in AdjList[i]:
        print(" --> {}".format(j), end=" ")
    print()
