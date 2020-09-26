# List-based implementation of Queue data structure
class Queue:
	# Initialize the queue as an empty list
	def __init__(self):
		self.queue = []

	# Check if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# Append an element at the end of the list, i.e., at the front of the queue
	def enqueue(self, val):
		self.queue.append(val)

	# Remove the front element of the queue, if the queue is not empty
	def dequeue(self):
		if not self.isEmpty():
			return self.queue.pop(0)

	# Return the front element without removing it
	def peek(self):
		if not self.queue.isEmpty():
			return self.queue[0]

# Test it
if __name__ == "__main__":
	queue = Queue()
	queue.enqueue(0)
	queue.enqueue(5)
	queue.enqueue(90)
	print(str(queue.dequeue()))
	print(queue.isEmpty())
	queue.dequeue()
	print(str(queue.dequeue()))

