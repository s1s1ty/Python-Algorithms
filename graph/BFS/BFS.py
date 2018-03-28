from collections import deque

class BFS(object):
	"""Basic Matrix implementation of BFS"""
	SIZE = 10
	def __init__(self):
		self.visited = [0]*BFS.SIZE
		self.cost = [0]*BFS.SIZE
		self.am = []
		for i in range(BFS.SIZE):
			self.temp = []
			for j in range(BFS.SIZE):
				self.temp.append(0)
			self.am.append(self.temp)

	def bfs(self, source):
		self.que = deque([])
		self.visited[source] = 1
		self.que.append(source)

		while self.que:
			u = self.que.popleft()
			for v in range(BFS.SIZE):
				if self.am[u][v] == 1 and self.visited[v]==0:
					self.visited[v] = 1
					self.que.append(v)
					self.cost[v] = self.cost[u]+1 

	def cost_print(self, destination):
		return self.cost[destination]
