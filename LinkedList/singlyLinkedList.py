"""
Implement Singly Linked List
"""

class Node(object):
    def __init__(self, _data, _next=None, _prev=None):
        self._data = _data
        self._next = _next
    
class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insertFirst(self, data):
        newNode = Node(data)
        newNode._next = self.head
        self.head = newNode
            
    def insertLast(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        temp = self.head
        while temp._next != None:
            temp = temp._next
        temp._next = Node(data)
        
    def insertNth(self, data, position):
        newNode = Node(data)
        temp = self.head
        if position == 0:
            self.head = newNode
            return
        for _ in range(position-1):
            temp = temp._next
            if temp == None:
                break
        newNode._next = temp._next
        temp._next = newNode
    
    def delete(self, position):
        if self.head is not None:
            temp = self.head
            for _ in range(position-1):
                temp = temp._next
                if temp == None:
                    break
            temp2 = temp._next
            temp._next = temp2._next
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def show(self):
        return self._show(self.head)
    
    def _show(self, head):
        if head == None: return
        print head._data
        self._show(head._next)
        
if __name__ == '__main__':
    print "executing"
    ob = LinkedList()
    ob.insertFirst(1)
    ob.insertLast(2)
    ob.insertLast(3)
    ob.delete(2)
    ob.show()

        

