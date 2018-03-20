import heapq

class Dijkstra(object):
	"""Implemented as adjucency matrix"""

	def __init__(self, vertex):
		self.vertex = vertex
		self.sortestPath = []
		self.cost = [float("inf")]*vertex
		self.par = [0]*vertex
		self.adjacency_matrix = [[float("inf") for _ in range(vertex)] for _ in range(vertex)] # 2d array initialize

	def dijkstra(self, s):
		self.cost[s] = 0
		self.que = []

		heapq.heappush(self.que, s)

		while self.que:
			u = heapq.heappop(self.que)
			for v in range(self.vertex):
				if self.adjacency_matrix[u][v]:
					if self.cost[v] > self.cost[u]+self.adjacency_matrix[u][v]:
						self.cost[v] = self.cost[u]+self.adjacency_matrix[u][v]
						self.par[v] = u
						heapq.heappush(self.que, v)

	def pathPrint(self, node):
		if node == 0: return
		self.pathPrint(self.par[node])
		self.sortestPath.append(node)
