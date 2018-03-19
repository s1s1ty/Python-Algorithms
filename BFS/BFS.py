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

	def bfs(self, souce):
		self.que = deque([])
		self.visited[souce] = 1
		self.que.append(souce)

		while self.que:
			u = self.que.popleft()
			for v in range(BFS.SIZE):
				if self.am[u][v] == 1 and self.visited[v]==0:
					self.visited[v] = 1
					self.que.append(v)
					self.cost[v] = self.cost[u]+1 

	def cost_print(self, destination):
		return self.cost[destination]

if __name__ == '__main__':
	ob = BFS()

	source = int(raw_input("Source: "))
	destination = int(raw_input("Destination: "))

	n = int(raw_input())

	for i in range(n):
		tmp = raw_input()
		u, v = tmp.split()
		u = int(u)
		v = int(v)
		ob.am[u][v] = ob.am[v][u] = 1

	# ob.am[1][2] = 1
	# ob.am[1][3] = 1
	# ob.am[1][5] = 1
	# ob.am[3][5] = 1
	# ob.am[8][4] = 1
	# ob.am[2][8] = 1
	# ob.am[3][4] = 1

	ob.bfs(source)
	print ob.cost_print(destination)
