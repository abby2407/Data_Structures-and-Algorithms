


# --------*-----Adjacency List using Dictionaries for Directed Graph !.-------*---------


class Vertex:
    def __init__(self,data):
        self.vertex = data
        self.connectedTo = {}

    def addNeighbor(self,vert,weight):
        self.connectedTo[vert] = weight

    def getConnections(self):
        return self.connectedTo
    
    def getVertex(self):
        return self.vertex

    def getWeight(self,temp):
        return self.connectedTo[temp]


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.noOfVertices = 0

    def addVertices(self,data):
        self.noOfVertices = self.noOfVertices + 1
        newVertex = Vertex(data)
        self.vertexList[data] = newVertex

    def addEdge(self,src,dest,weight = 0):
        if src not in self.vertexList:
            self.addVertices(src)
        if dest not in self.vertexList:
            self.addVertices(dest)
        self.vertexList[src].addNeighbor(self.vertexList[dest],weight)

    def print_graph(self):
        for v in self.vertexList.values():
            print("Adjacency list of {} are".format(v.getVertex()))
            for w in v.getConnections():
                print("> {} ".format(w.getVertex()))


# ------------------ Breadth First Search or BFS for a Graph ! -------------------
    def BFS(self,startNode):
        visited = []
        queue = []
        queue.append(startNode)

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for ver in self.vertexList.values():
                    if ver.getVertex() == node:
                        cur_node = ver
                        for neighbour in cur_node.getConnections():
                            queue.append(neighbour.getVertex())
        return visited


# ------------------ Depth First Search or DFS for a Graph - Using a Recursive approach! -------------------
    def DFS(self,startNode):
        visited = [False] * (len(self.vertexList))

        self.DFSutil(startNode,visited)

    def DFSutil(self,cur_node,visited):
        visited[cur_node] = True
        print(cur_node, end=" ")
        for ver in self.vertexList.values():
            if ver.getVertex() == cur_node:
                node = ver
                for neighbour in node.getConnections():
                    n = neighbour.getVertex()
                    if visited[n] == False:
                        self.DFSutil(n,visited)


# ------------------ Depth First Search or DFS for a Graph - Using Iterative approach! -------------------
    def DFS2(self, startNode):
        visited = [False] * (len(self.vertexList))

        stack = []
        stack.append(startNode)

        while (len(stack)):
            cur_node = stack.pop()
            if visited[cur_node] == False:
                print(cur_node,end=" ")
                visited[cur_node] = True
            
            for ver in self.vertexList.values():
                if ver.getVertex() == cur_node:
                    node = ver
                    for neighbour in node.getConnections():
                        n = neighbour.getVertex()
                        if visited[n] == False:
                            stack.append(n)


# ------------------ Testing the Graph Traversal Methods -----------------
g = Graph()
for i in range(4):
    g.addVertices(i)

g.addEdge(0,1,5)
g.addEdge(0,2,2)
g.addEdge(1,0,4)
g.addEdge(1,3,9)
g.addEdge(1,4,7)
g.addEdge(2,0,3)
g.addEdge(3,1,1)
g.addEdge(4,2,8)
g.addEdge(4,3,1)

g.print_graph()
print()

print("BFS Traversal of the given Graph is : ",g.BFS(3))

print("DFS Traversal of the given Graph using Recursive approach is : ",end=" ")
g.DFS(3)

print()

print("DFS Traversal of the given Graph using Iterative Approach is : ",end=" ")
g.DFS2(3)

