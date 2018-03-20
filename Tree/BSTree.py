class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.value = data
		self.left=left
		self.right=right


class BSTree(object):
	"""Insert Print and Delete Binery Search tree implementation"""
	def __init__(self):
		self.all_element = []
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
			self.all_element = []
			self._printPreorder(self.root)
			return self.all_element

	def _printPreorder(self, cur_node):
		if cur_node != None:
			self.all_element.append(cur_node.value)
			self._printPreorder(cur_node.left) 
			self._printPreorder(cur_node.right) 

	def printInorder(self):
		if self.root != None:
			self.all_element = []
			self._printInorder(self.root)
			return self.all_element

	def _printInorder(self, cur_node):
		if cur_node != None:
			self._printInorder(cur_node.left) 
			self.all_element.append(cur_node.value)
			self._printInorder(cur_node.right) 

	def printPostorder(self):
		if self.root != None:
			self.all_element = [] # if any element assign before
			self._printPostorder(self.root)
			return self.all_element

	def _printPostorder(self, cur_node):
		if cur_node != None:
			self._printPostorder(cur_node.left) 
			self._printPostorder(cur_node.right) 
			self.all_element.append(cur_node.value)

	# Calculate Depth of the Tree
	def MaxDepth(self):
		if self.root == None:
			return 0
		return self._max_depth(self.root, 0)

	def _max_depth(self, cur_node, cur_dep):
		if cur_node == None:
			return cur_dep
		else:
			digLeft = self._max_depth(cur_node.left, cur_dep+1)
			digRight = self._max_depth(cur_node.right, cur_dep+1)
			return max(digRight, digLeft)

	def MinDepth(self):
		if self.root == None:
			return 0
		return self._min_depth(self.root)

	def _min_depth(self, root):
		if root == None:
			return 0
		if root.right == None and root.left== None:
			return 1
		if root.left == None:
			return self._min_depth(root.right)+1
		if root.right == None:
			return self._min_depth(root.left)+1
		return min(self._min_depth(root.right), self._min_depth(root.left))+1



