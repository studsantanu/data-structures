# List-based implementation of stack data structure
class Stack:
	# Initialize the stack as an empty list
	def __init__(self):
		self.stack = []

	# Check if the stack is empty
	def isEmpty(self):
		return len(self.stack) == 0

	# Append a new value at the end of the list, i.e., on the top of the stack
	def push(self, val):
		self.stack.append(val)

	# Remove the top element of the stack and return it, if the stack is not empty
	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()

	# Return the top element without removing it
	def peek(self):
		if not self.isEmpty():
			return self.stack[-1]

# Test it
if __name__ == "__main__":
	stack = Stack()
	stack.push(1)
	stack.push(54)
	stack.push(43)
	stack.push(3)
	print(str(stack.pop()))
	stack.push(5)
	stack.pop()
	stack.push(2)
	print(str(stack.peek()))
	stack.pop()
	stack.pop()
	stack.pop()
	print(str(stack.pop()))
	print(stack.isEmpty())

