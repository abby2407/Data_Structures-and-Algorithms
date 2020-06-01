

# ------------------ Python program to find minimum edges between SRC nad DEST in an Undirected Graph -------------------

class minEdgesGraph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.matrix = [[0 for x in range(self.number_of_nodes)] for y in range(self.number_of_nodes)]								

    def addEdge(self, node1, node2):
        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1


# ------------------ Function to find minimum no. of edge between two vertex of Graph using DFS -----------------    
    def minEdges(self,src,dest):
        visited = [False] * self.number_of_nodes
        minNumOfEdges = 0
        edgesCount = 0
        
        minNumOfEdges, edgesCount = self.minEdgesDFS(src, dest, visited, minNumOfEdges, edgesCount)
        
        print("Minimum Number of Edges between SRC and DEST is :",minNumOfEdges)
        
        
    def minEdgesDFS(self, src, dest, visited, minNumOfEdges, edgesCount):
        visited[src] = True
        if src == dest:
            if minNumOfEdges > edgesCount:
                minNumOfEdges = edgesCount
            else:
                minNumOfEdges = edgesCount
        else:
            for row in range(self.number_of_nodes):
                if self.matrix[src][row] == 1:
                    if visited[row] == False:
                        edgesCount += 1
                        minNumOfEdges, edgesCount = self.minEdgesDFS(row, dest, visited, minNumOfEdges, edgesCount)
        visited[src] = False
        edgesCount -= 1
        return minNumOfEdges, edgesCount


# ------------------ Function to find minimum no. of edge between two vertex of Graph using BFS -----------------
'''    def minEdgeBFS(self,src,dest):
        visited = [False] * self.number_of_nodes
        edgeCount = 0
        minNumOfEdges = 0
        queue = []
        
        queue.append(src)
        visited[src] = True
        while len(queue) != 0:
            x = queue.pop(0)
            for i in range(self.number_of_nodes):
                if self.matrix[x][i] == 1 and visited[i] == False:
                    if src == dest:
                        if minNumOfEdges == 0:
                            minNumOfEdges = edgeCount
                        elif minNumOfEdges > edgeCount:
                            minNumOfEdges = edgeCount
                            break
                    else:
                        edgeCount += 1
                        visited[i] = True
                        queue.append(i)

            edgeCount -= 1
            visited[x] = False
        print(minNumOfEdges)'''


graph = minEdgesGraph(10)
graph.addEdge(0, 1)  
graph.addEdge(0, 7)  
graph.addEdge(1, 7)  
graph.addEdge(1, 2)  
graph.addEdge(2, 3)  
graph.addEdge(2, 5)  
graph.addEdge(2, 8)  
graph.addEdge(3, 4)  
graph.addEdge(3, 5)  
graph.addEdge(4, 5)  
graph.addEdge(5, 6)  
graph.addEdge(6, 7)  
graph.addEdge(7, 8) 
graph.minEdges(0,6)