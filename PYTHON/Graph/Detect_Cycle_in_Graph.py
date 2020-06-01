
# --------*----- python program to Detect Cycle in a Directed Graph using DFS !.-------*---------


from collections import defaultdict, deque

class DirectedGraph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)                      # list of Pointers to Adjacent Nodes
        self.vertices = vertices                            # no. of Vetices in Graph

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def detectCycle(self):
        visited = [False] * self.vertices
        recStack = [False] * self.vertices

        for v in range(self.vertices):
            if visited[v] == False:
                if self.detectCycleUtil(v,visited,recStack) == True:
                    print("CYCLE EXIST for the given Directed Graph ! ")
                    return True
        return False
               
    def detectCycleUtil(self, node, visited, recStack):
        visited[node] = True
        recStack[node] = True

        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.detectCycleUtil(neighbour,visited,recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        
        recStack[node] = False
        return False


g = DirectedGraph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.detectCycle()



# --------*----- Python Program to detect cycle in an undirected graph using DFS !.-------*---------

#  We do a DFS traversal of the given graph. For every visited vertex ‘v’, if there is an 
# adjacent ‘u’ such that u is already visited and u is not parent of v, then there is a cycle in graph

class UnDirectedGraph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def detectCycle1(self):
        visited = [False] * self.vertices
        for i in range(self.vertices):
            if visited[i] == False:
                if self.detectCycleDFS(i,visited,-1) == True:
                    return True
        return False

    def detectCycleDFS(self,node,visited,parent):
        visited[node] = True
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.detectCycleDFS(neighbour,visited,node) == True:
                    return True
            elif neighbour != parent:
                return True
        return False

# --------*----- Python Program to detect cycle in an undirected graph using BFS !.-------*---------

    def detectCycle2(self):
        visited = [False] * self.vertices
        for i in range(self.vertices):
            if visited[i] == False:
                if self.detectCycleBFS(i,visited) == True:
                    return True
        return False

    def detectCycleBFS(self, node, visited):
        visited[node] = True
        parent = [-1] * self.vertices

        q = deque()
        q.append(node)

        while q:
            cur_node = q.pop()
            for v in self.graph[cur_node]:
                if visited[v] == False:
                    q.append(v)
                    visited[v] = True
                    parent[v] = cur_node
                elif parent[v] != cur_node:
                    return True

        return False


g = UnDirectedGraph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,0)
g.addEdge(3,1)
g.addEdge(4,2)
g.addEdge(4,3)
print("Does Cycle exist for the given Undirected Graph Using DFS : ",g.detectCycle1())
print("Does Cycle exist for the given Undirected Graph Using BFS : ",g.detectCycle2())