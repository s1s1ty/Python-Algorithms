'''
Shaonty Dutta
Python BFS Implementation
Time complexity O(v+e)
'''

from collections import deque, defaultdict


class BFS(object):
	"""List implementation of BFS"""
	def __init__(self):
		self.cost = defaultdict(int)
	
	def bfs(self, graph, source):
		visited, queue = set(), deque([source])
		visited.add(source)
		self.cost[source] = 0

		while queue:
			node = queue.popleft()
			for neighbour in graph[node]:
				if neighbour not in visited:
					visited.add(neighbour)
					queue.append(neighbour)
					self.cost[neighbour] = self.cost[node] + 1
	
	def cost_print(self, destination):
		return self.cost[destination]
	

class BFSM(object):
	"""Basic Matrix implementation of BFS"""
	SIZE = 10
	def __init__(self):
		self.cost = [0]*BFSM.SIZE
		self.am = []
		for i in range(BFSM.SIZE):
			self.temp = []
			for j in range(BFSM.SIZE):
				self.temp.append(0)
			self.am.append(self.temp)

	def bfs(self, source):
		visited, queue = set(), deque([source])
		visited.add(source)

		while queue:
			u = queue.popleft()
			for v in range(BFSM.SIZE):
				if self.am[u][v] == 1 and v not in visited:
					visited.add(v)
					queue.append(v)
					self.cost[v] = self.cost[u]+1 

	def cost_print(self, destination):
		return self.cost[destination]
