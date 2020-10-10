"""Module for Trie datastructure"""

class Node:
    def __init__(self, char):
        self._char = char
        self._is_end = False
        self.child = {}

class Trie:
    def __init__(self):
        self._node = Node("")
    
    def insert(self, word):
        root = self._node
        for char in word:
            if char in root.child:
                root = root.child[char]
            else:
                new_node = Node(char)
                root.child[char] = new_node
                root = new_node    
        root._is_end = True

    def all_prefix(self, prefix):
        root = self._node
        for char in prefix:
            if char in root.child:
                root = root.child[char]
            else:
                return []
        return self.__search(root, prefix, [])

    def __search(self, node, prefix, output):
        if node._is_end:
            output.append(prefix)
        for child in node.child.values():
            self._search(child, prefix + child._char, output)

        return output

ob = Trie()

ob.insert("apple")
ob.insert("app")
ob.insert("applism")
print(ob.all_prefix("ap"))
print(ob.all_prefix("b"))