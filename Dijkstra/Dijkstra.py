import heapq

class Dijkstra(object):
	"""Implemented as adjucency matrix"""
	SIZE = 10
	def __init__(self):
		self.sortestPath = []
		self.cost = [100]*Dijkstra.SIZE
		self.par = [0]*Dijkstra.SIZE
		self.am = []
		for i in range(Dijkstra.SIZE): 
			self.temp = []
			for j in range(Dijkstra.SIZE):
				self.temp.append(100)
			self.am.append(self.temp)

	def dijkstra(self, s):
		self.cost[s] = 0
		self.que = []

		heapq.heappush(self.que, s)

		while self.que:
			u = heapq.heappop(self.que)
			for v in range(Dijkstra.SIZE):
				if self.am[u][v]!=100:
					if self.cost[v] > self.cost[u]+self.am[u][v]:
						self.cost[v] = self.cost[u]+self.am[u][v]
						self.par[v] = u
						heapq.heappush(self.que, v)

	def pathPrint(self, node):
		if node == 0: return
		self.pathPrint(self.par[node])
		self.sortestPath.append(node)
