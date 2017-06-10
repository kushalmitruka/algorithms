"""
Build and Implement LinkedList Datastructure, Assumption `Not a circular/cyclic linkedlist`
"""

class singleLinkedList(object):

	_head = None

	# Operations for a linked list
	# 	insert an element
	# 	remove an element
	#	search for a element
	#	move to a particular index


	@property
	def head(self):
		return self._head

	@head.setter
	def head(self, value):
		if isinstance(value, Node):
			self._head = value
			return 'Head Set to {}'.format(value)


	def insert_value_at_end(self, value):
		node = self.head
		while(node.next_node is not None):
			node = node.next_node
		
		node.next_node = Node()
		node = node.next_node
		node.value = value

		return 'Value added at the End'

	def insert_value_at_start(self, value):
		node = self.head
		self.head = Node()
		self.head.value = value
		self.head.next_node = node

		return 'Value added at the Start'

	def insert_value_at_index(self, value, index):
		node = self.head
		if (index == 1):
			return self.insert_value_at_start()

		for i in range(index-2):
			node = node.next_node
		
		if node.next_node is None:
			return self.insert_value_at_end()
		new_node = Node()
		new_node.value = value
		new_node.next_node = node.next_node
		node.next_node = new_node

		return 'Inserted value at index: {}'.format(index)	

	def remove_value_from_start(self):
		node = self.head
		self.head = node.next_node

		return 'Removed Node: {}'.format(node)

	def remove_value_from_end(self):
		node = self.head
		prev_node = None
		while(node.next_node is not None):
			prev_node = node
			node = node.next_node
		
		prev_node.next_node = None

		return 'Removed Node: {}'.format(node)
		
	def remove_value_from_index(self, index):
		node = self.head
		if index == 1:
			return self.remove_value_from_start()
		for i in range(index-2):
			node = node.next_node

		remove_node = node.next_node
		next_node = node.next_node.next_node
		node.next_node = next_node

		return 'Removed Node: {}'.format(remove_node)

	def search_value(self, value):
		node = self.head
		index = 1
		while(node is not None):
			if node.value == value:
				return 'Value found at Index: {}'.format(index)
			node = node.next_node
			index += 1
		return 'Value dosen;t exists'

	def return_value_at_index(self, index):
		node = self.head
		if index == 1:
			return self.head.value
		
		for i in range(index-1):
			node = node.next_node
		
		return node.value

	@property
	def length(self):
		index = 0
		if self.head.value is not None:
			index += 1
		
		node = self.head
		while(node.next_node is not None):
			node = node.next_node
			index += 1

		return index
	
	def __str__(self):
		str_rep = ''
		node = self.head
		if self.head.value is not None:
			str_rep += str(self.head)

		while(node.next_node is not None):
			node = node.next_node
			str_rep += str(node)

		return '{}'.format(str_rep)


class Node(object):

	_value = None
	_next_node = None

	@property
	def next_node(self):
		return self._next_node

	@next_node.setter
	def next_node(self, value):
		if isinstance(value, Node):
			self._next_node = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	def __str__(self):
		return '[{}]{}'.format(self.value, '-->' if self.next_node else '')
