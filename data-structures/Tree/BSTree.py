'''
Shaonty Dutta
Binary Search Tree Implementation in Python
'''
from collections import deque


class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left=left
		self.right=right


class BSTree(object):
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		# new_node = 
		self.__insert(self.root, Node(data))
	
	def __insert(self, root, new_node):
		if root is None:
			self.root = new_node
		else:
			if root.data > new_node.data:
				if root.left is None:
					root.left = new_node
				else:
					self.__insert(root.left, new_node)
			else:
				if root.right is None:
					root.right = new_node
				else:
					self.__insert(root.right, new_node)
 
	def search(self, data):
		self.__search(self.root, data)
	
	def __search(self, cur_node, data):
		if cur_node is None:
			return False
		elif data is cur_node.data:
			return True
		elif data < cur_node.data:
			self.__search(cur_node.left, data)
		else:
			self.__search(cur_node.right, data)

	def remove(self):
		pass
	
	def level_order(self):
		if self.root != None:
			cur_node = self.root
			queue, all_element = deque([cur_node]), []

			while len(queue) > 0:
				cur_node = queue.popleft()
				all_element.append(cur_node.data)

				if cur_node.left:
					queue.append(cur_node.left)

				if cur_node.right:
					queue.append(cur_node.right)

			return all_element

	def pre_order(self):
		if self.root != None:
			return self.__pre_order(self.root, [])
		
	def __pre_order(self, cur_node, all_element):
		if cur_node != None:
			all_element.append(cur_node.data)
			self.__pre_order(cur_node.left, all_element) 
			self.__pre_order(cur_node.right, all_element) 
		return all_element

	def in_order(self):
		if self.root != None:
			return self.__in_order(self.root, [])

	def __in_order(self, cur_node, all_element):
		if cur_node != None:
			self.__in_order(cur_node.left, all_element) 
			all_element.append(cur_node.data)
			self.__in_order(cur_node.right, all_element) 
		return all_element

	def post_order(self):
		if self.root != None:
			return self.__post_order(self.root, [])

	def __post_order(self, cur_node, all_element):
		if cur_node != None:
			self.__post_order(cur_node.left, all_element) 
			self.__post_order(cur_node.right, all_element) 
			all_element.append(cur_node.data)
		return all_element

	# Calculate height of the Tree
	def height(self):
		if self.root == None:
			return 0
		return self.__height(self.root, 0)

	def __height(self, cur_node, cur_dep):
		if cur_node == None:
			return cur_dep
		else:
			digLeft = self.__height(cur_node.left, cur_dep+1)
			digRight = self.__height(cur_node.right, cur_dep+1)
			return max(digRight, digLeft)

	def Minheight(self):
		if self.root == None:
			return 0
		return self._min_height(self.root)

	def _min_height(self, root):
		if root == None:
			return 0
		if root.right == None and root.left== None:
			return 1
		if root.left == None:
			return self._min_height(root.right)+1
		if root.right == None:
			return self._min_height(root.left)+1
		return min(self._min_height(root.right), self._min_height(root.left))+1






