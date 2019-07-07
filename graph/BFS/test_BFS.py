import unittest
import collections
from BFS import BFSM, BFS

class BFSTestCase(unittest.TestCase):
    def test(self):
        ob = BFS()
        graph = collections.defaultdict(set)
        graph[1] = [2, 3, 5]
        graph[2] = [8]
        graph[3] = [5,4]
        graph[8] = [4]
        source = 2
        destination = 4
        
        ob.bfs(graph, source)
        self.assertEqual(ob.cost_print(destination), 2, msg="Cost should be 2")


class BFSMTestCase(unittest.TestCase):
    """ Test for BFS.py"""
    def test(self):
        ob = BFSM()
        # test data 
        ob.am[1][2] = 1
        ob.am[1][3] = 1
        ob.am[1][5] = 1
        ob.am[3][5] = 1
        ob.am[8][4] = 1
        ob.am[2][8] = 1
        ob.am[3][4] = 1
        source = 1
        destination = 4
        ob.bfs(source)
        self.assertEqual(ob.cost_print(destination), 2, msg="Cost should be 2")

if __name__ == '__main__':
    unittest.main()

