
''' A mother vertex in a graph G = (V,E) is a vertex v such that all 
    other vertices in G can be reached by a path from v.'''



from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def DFS(self, node, visited):
        visited[node] = True

        for n in self.graph[node]:
            if visited[n] == False:
                self.DFS(n, visited)


# ------------------ Method to find a Mother Vertex in a Graph -------------------
    def findMother(self):
        visited = [False] * self.vertices
        
        v = 0

        for i in range(self.vertices):
            if visited[i] == False:
                self.DFS(i, visited)
                v = i

        visited = [False] * self.vertices
        self.DFS(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v


# ------------------ Testing the Program -----------------
g = Graph(7) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0) 

print("Mother vertex is: {} ".format(g.findMother()))