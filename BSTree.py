class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.value = data
		self.left=left
		self.right=right


class BSTree(object):
	"""Insert Print and Delete Binery Search tree implementation"""
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root==None:
			self.root = Node(value)
			return True
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value <= cur_node.value:
			# left e jabe
			if cur_node.left==None:
				cur_node.left = Node(value)
			else:
				self._insert(value, cur_node.left)
		else:
			# right e jabe
			if cur_node.right == None:
				cur_node.right = Node(value)
			else:
				# because of find leaf node then insert
				self._insert(value, cur_node.right)

	# print different order
	def printPreorder(self):
		if self.root != None:
			self._printPreorder(self.root)

	def _printPreorder(self, cur_node):
		if cur_node != None:
			print cur_node.value
			self._printPreorder(cur_node.left) 
			self._printPreorder(cur_node.right) 

	def printInorder(self):
		if self.root != None:
			self._printInorder(self.root)

	def _printInorder(self, cur_node):
		if cur_node != None:
			self._printInorder(cur_node.left) 
			print cur_node.value
			self._printInorder(cur_node.right) 

	def printPostorder(self):
		if self.root != None:
			self._printPostorder(self.root)

	def _printPostorder(self, cur_node):
		if cur_node != None:
			self._printPostorder(cur_node.left) 
			self._printPostorder(cur_node.right) 
			print cur_node.value

	# Calculate Depth of the Tree
	def depth(self):
		if self.root == None:
			return 0
		return self._depth(self.root, 0)

	def _depth(self, cur_node, cur_dep):
		if cur_node == None:
			return cur_dep
		else:
			digLeft = self._depth(cur_node.left, cur_dep+1)
			digRight = self._depth(cur_node.right, cur_dep+1)
			return max(digRight, digLeft)




print "Bs tree starting...."
tree = BSTree()
# let some value for creating bs tree
num = [11, 6, 15, 3, 8, 13, 17, 12, 14, 19, 1, 5]
for i in num:
	tree.insert(i)

print "Inorder Traversal order: "
tree.printInorder()

print "Depth Of The Tree: {}".format(tree.depth())


