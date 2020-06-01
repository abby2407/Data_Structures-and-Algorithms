
'''The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. 
   The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.'''



class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
INF = 99999
class Graph:
    def __init__(self):
        self.adj = {} #Adjacency matrix that holds graph data
        self.vertexCount = 0

    def addVertex(self, vertex):
        if vertex in self.adj:
            return "Vertex already exists"
        if vertex != self.vertexCount:
            return "Don't skip a vertex"
        self.adj[vertex] = []
        self.vertexCount += 1

    def addEdge(self, start, end, weight):
        if start not in self.adj:
            return "Starting vertex not in graph"
        if end not in self.adj:
            return "Ending vertex not in graph"
        if start == end:
            return "Cannot have same start and end vertex"
        edge = Edge(start, end, weight)
        self.adj[start].append(edge)

    def doesEdgeExist(self, start, end):
        for vertex in self.adj:
            for edge in self.adj[vertex]:
                if edge.start == start and edge.end == end:
                    return (True, edge)
        return (False, None)

    def floydwarshall(self):
        M = [[INF for x in range(len(self.adj))] for y in range(len(self.adj))]
        for x in range(len(M)):
            for y in range(len(M[0])):
                if x == y:
                    M[x][y] = 0
                exists, edge = self.doesEdgeExist(x, y)
                if exists:
                    M[x][y] = edge.weight
        for k in range(len(M)):
            for i in range(len(M)):
                for j in range(len(M)):
                    newDistance = M[i][k] + M[k][j]
                    if newDistance < M[i][j]:
                        M[i][j] = newDistance
        
        self.printSolution(M)
        return M

# --------*----- Transitive Closure of a Graph using Floyd Warshall Algorithm !.-------*---------
# The graph is given in the form of adjacency matrix say ‘graph[V][V]’ 
# where graph[i][j] is 1 if there is an edge from vertex i to vertex j or i is equal to j, otherwise graph[i][j] is 0.

    """ def transitiveClosure(self):
		tempMatrix = [i[:] for i in self.adj]
        for k in range(self.number_of_nodes):
			for i in range(self.number_of_nodes):
				for j in range(self.number_of_nodes):
					tempMatrix[i][j] = tempMatrix[i][j] or (tempMatrix[i][k] and tempMatrix[k][j])
		self.printSolution(tempMatrix) """


    def printSolution(self,temp): 
        for vertex in self.adj:
            for edge in temp[vertex]:
                if edge == 99999:
                    print("%7s" %("INF"),end=" ")
                else:
                    print("%7d" %(edge),end=" ")
            print(" ")

g = Graph()

for i in range(0,7):
    g.addVertex(i)

g.addEdge(0, 1, 5) 
g.addEdge(0, 2, 2) 
g.addEdge(1, 3, 4) 
g.addEdge(4, 1, 9) 
g.addEdge(6, 4, 7) 
g.addEdge(5, 6, 3) 
g.addEdge(5, 2, 1) 
g.addEdge(6, 0, 8)

g.floydwarshall()