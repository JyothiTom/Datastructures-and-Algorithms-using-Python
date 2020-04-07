"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementing the data-structure queue using python.
"""

class queue(object):

	def __init__(self):
		self.queue_content = []

	def push(self, item):
		self.queue_content.append(item)

	def pop(self):
		self.queue_content.pop(0)


q = queue()

q.push(10)
print(q.queue_content)

q.push(11)
print(q.queue_content)

q.push(12)
print(q.queue_content)

q.pop()
print(q.queue_content)