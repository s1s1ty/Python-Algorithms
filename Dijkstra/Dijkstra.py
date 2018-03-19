# Implemented as adjucency matrix

import heapq

class Dijkstra(object):
	SIZE = 10

	def __init__(self):
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
		print node,

if __name__ == '__main__':
	djk = Dijkstra()
	source = int(raw_input("source: "))
	destination = int(raw_input("destination: "))

	# n = int(raw_input())

	# for i in range(n):
	# 	tmp = raw_input()
	# 	u, v, w = tmp.split()
	# 	u = int(u)
	# 	v = int(v)
	# 	w = int(w)
	# 	djk.am[u][v] = djk.am[v][u] = w

	djk.am[1][2] = djk.am[2][1] = 2
	djk.am[1][4] = djk.am[4][1] = 1
	djk.am[2][3] = djk.am[3][2] = 4
	djk.am[2][5] = djk.am[5][2] = 5
	djk.am[3][5] = djk.am[5][3] = 1
	djk.am[3][4] = djk.am[4][3] = 3

	djk.dijkstra(source)
	if djk.cost[destination] == 100:
		print -1
	else:
		print "Sortest Path: ",
		djk.pathPrint(destination)
