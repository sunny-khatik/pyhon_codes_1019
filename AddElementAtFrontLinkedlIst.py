# Python3 code to move the last item to front
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		tmp = self.head
		while tmp is not None:
			print(tmp.data, end=", ")
			tmp = tmp.next
		print()
	def moveToFront(self):
	    if self.head is None:
	        return
	    if self.head.next is None:
	        return
	    prev=None
	    tmp=self.head
	    while tmp.next:
	        prev=tmp
	        tmp = tmp.next
	    prev.next=None
	    tmp.next=self.head
	    self.head=tmp
	    
if __name__ == '__main__':
	llist = LinkedList()
	
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)
	print ("Linked List before moving last to front ")
	llist.printList()
	llist.moveToFront()
	print ("Linked List after moving last to front ")
	llist.printList()
