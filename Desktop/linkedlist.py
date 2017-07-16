class Node():
	def __init__ (self,data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)+ ">" + str(self.next)

	'''Get and Set methods for this class'''

	def getData(self):
		return self.data
	def setData(self,newdata):
		self.data = newdata
	def getNext(self):
		return self.next
	def setNext(self,next):
		self.next = next

class LinkedList():
	'''We create a list of nodes using the LinkedList class'''
	def __init__(self):
		self.head = None

	def size(self):
		'''This method tells you how many values are in the linked
		list'''
		index = 0
		count = 0
		currNode = self.head
		while currNode != None:
			currNode = currNode.getNext()
			count +=1
			index = count
			
		return "There are currently " + str(count) + " items in the linked list"

	def index_Item(self,item):
		'''This method gets the index of any item you
		search for in the linked list'''
		currNode = self.head
		index =1
		found = False
		while currNode != None and not found:
			if currNode.getData()== item:
				found = True
				if found and index == 0:
					return "item is first in list"
				else:
					return ("The item you searched for is " + str(item),"and its at pos " + str(index))
			elif not found and currNode.getNext()== None:
				return str(item) + " Not in list" 
			else:
				currNode = currNode.getNext()
				index+=1
		
		

	def addNode(self,data):
		'''Adds a node at head of list.'''
		node = Node(data)#creates new node
		node.setNext(self.head)#links to the next node in the series,if there is no node this val is None
		self.head = node#resets the head to point to the first item in the list
		return node
		# print(node.getNext())
		
		
	def search(self,item):
		'''traverses list starting from node and searches for requested value
		return True if found and False if not found'''
		currNode = self.head
		found = False
		while currNode != None and not found:
			if currNode.data == item:
				found = True
			else:
				currNode = currNode.getNext()
		return found

	def deleteNode(self,item):
		'''Delets node'''
		currNode = self.head
		prevNode = None
		found = False
		while currNode != None and not found:
			if currNode.getData()==item:
				found = True
			else:
				prevNode = currNode
				currNode = currNode.getNext()
		if found == False:
			print("Not found member " + str(item))
		else:
			if prevNode == None:
				self.head = currNode.getNext()
			else:

				prevNode.setNext(currNode.getNext())

				print("succesfully deleted " + str(currNode.data))
	def appendNode(self,item):
		'''Add a value at end of linked list
		We start at head and traverse through list till the end
		we then add a new node there'''
		currNode = self.head
		end_of_list = False
		while currNode!=None and not end_of_list:
			currNode = currNode.getNext()
			if currNode.getNext() == None:
				end_of_list = True
		newnode = Node(item)
		currNode.setNext(newnode)
		print("Appended new node with value " + str(item) + " at end of linked list")

	def insert_Node(self,newnode,position):
		'''This Method allows you to insert the node at any position 
		you want in the linked list, returns error if you put invalid index for inserting your new node'''
		currNode = self.head
		index =1
		found = False
		prevNode = None
		if position == 1:
			node = Node(newnode)
			self.head = node
			node.setNext(currNode)
			print("New Node with value " + str(newnode) + " has been inserted at position " + str(position))
		else:
			while currNode != None and not found:
					prevNode = currNode
					currNode = currNode.getNext()
					index+=1
					if index == position:
						found = True
						print(index,position)
						node = Node(newnode)
						prevNode.setNext(node)
						node.setNext(currNode)
						print("New Node with value " + str(newnode)+" has been added at pos " + str(position))
						return
					else:
						print("invalid index, the value " + str(newnode) + " has not added to list")
						return
		
					
l = LinkedList()
for i in range(1,10):
	l.addNode(i)
print(l.head)
l.insert_Node(7,5)
l.deleteNode(7)
l.deleteNode(6)
print(l.head)
print(l.size())
l.appendNode("My Dog")
l.insert_Node("boy",1)
print(l.head)
