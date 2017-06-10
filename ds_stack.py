"""
Implement stack datastructure and define `push` and `pop` methods on it
"""

class Stack(object):

	def __init__(self, size_of_stack):
		self.stack = ['#']*size_of_stack
		self.push_index = 0
		self.pop_index = 0

	def push(self, element):
		self.stack[self.push_index] = element
		self.push_index += 1

	def pop(self):
		element = self.stack[self.pop_index]
		self.stack[self.pop_index] = '#'
		self.pop_index -= 1
		return element

if __name__=='__main__':

	x = raw_input('>>')
	
	while (x != 'q'):
		print (eval(x))
		x = raw_input('>>')