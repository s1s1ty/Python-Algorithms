import unittest
from Dijkstra import Dijkstra

class DijkstraTestCase(unittest.TestCase):
    """ Test for Dijkstra.py"""
    def test(self):
        djk = Dijkstra(10)
        # test data 
        source = 1
        destination = 5
        djk.adjacency_matrix[1][2] = djk.adjacency_matrix[2][1] = 2
        djk.adjacency_matrix[1][4] = djk.adjacency_matrix[4][1] = 1
        djk.adjacency_matrix[2][3] = djk.adjacency_matrix[3][2] = 4
        djk.adjacency_matrix[2][5] = djk.adjacency_matrix[5][2] = 5
        djk.adjacency_matrix[3][5] = djk.adjacency_matrix[5][3] = 1
        djk.adjacency_matrix[3][4] = djk.adjacency_matrix[4][3] = 3
        
        djk.dijkstra(source)
        djk.pathPrint(destination)
        self.assertEqual(djk.sortestPath, [1,4,3,5], msg="Path Should be [1,4,3,5]")

if __name__ == '__main__':
    unittest.main()
