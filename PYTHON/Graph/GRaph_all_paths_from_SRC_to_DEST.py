

''' In this Program we are using DEPTH FIRST TRAVERSAL for finding all the paths from source
    to destination. Here we keep storing the current visited vertices in an array path[] and
    if we reach the destination vertex, then print the contents of the path'''


from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices                        # No. of vertices in a Graph
        self.graph = defaultdict(list)                  # List of Pointers to Adjacent Nodes


# ------------------ Inserting Node in a Directed Graph -------------------
    def add_Edge(self,src,dest):
        self.graph[src].append(dest)


# ------------------ Program to print All path from SOURCE to DESTINATION. -------------------
    def allPaths(self, src, dest):
        visited = [False] * self.vertices
        path = []

        self.printAllPaths(src, dest, visited, path)

    def printAllPaths(self, src, dest, visited, path):
        visited[src] = True
        path.append(src)

        if src == dest:
            print(path)
        else:
            for node in self.graph[src]:
                if visited[node] == False and node not in path:
                    self.printAllPaths(node, dest, visited, path)
        path.pop()
        visited[src] = False


# ------------------ Testing the Program -----------------
v = 4
graph = Graph(v)
graph.add_Edge(0,1)
graph.add_Edge(0,2)
graph.add_Edge(0,3)
graph.add_Edge(2,0)
graph.add_Edge(2,1)
graph.add_Edge(1,3) 
graph.allPaths(2,3)