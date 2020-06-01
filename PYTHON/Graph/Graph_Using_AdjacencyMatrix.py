
# ------------------ Python Program for creating Adjacency Matrix -------------------

class Graph:
	def __init__(self, number_of_nodes):
		self.number_of_nodes = number_of_nodes					# no. of Nodes in a Graph
		self.matrix = []										# Base Matrix
		self.create_matrix()									

	def create_matrix(self):
		for x in range(self.number_of_nodes):
			v = []
			for x in range(self.number_of_nodes):
				v.append(0)
			self.matrix.append(v)

	def addEdge(self, node1, node2):
		self.matrix[node1][node2] = 1
		self.matrix[node2][node1] = 1

	def printMatrix(self):
		for row in self.matrix:
			print(row)

# --------*-----Count total ways to reach destination from source in an undirected Graph !.-------*---------

	def totalWays(self,src,dest):
		visited = [False] * self.number_of_nodes
		
		visited[src] = True

		return self.countWays(src, dest,visited)

	def countWays(self,src,dest,visited):
		if src == dest:
			return 1
		total = 0
		for row in range(self.number_of_nodes):
			if self.matrix[src][row] == 1 and not visited[row]:
				visited[row] = True
				total += self.countWays(row,dest,visited)
				visited[row] = False

		return total


# ------------------ Testing the Graph -------------------
g = Graph(10)
g.addEdge(0,1)
g.addEdge(0,6)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(4,5)
g.addEdge(4,9)
g.addEdge(5,4)
g.addEdge(5,6)
g.addEdge(5,9)
g.addEdge(6,0)
g.addEdge(6,5)
g.addEdge(6,7)
g.addEdge(7,6)
g.addEdge(7,8)
g.addEdge(8,7)
g.addEdge(8,9)
g.addEdge(9,4)
g.addEdge(9,5)
g.addEdge(9,8)
g.printMatrix()
print()
print("total ways to reach DEST from SRC is :",g.totalWays(8,6))


