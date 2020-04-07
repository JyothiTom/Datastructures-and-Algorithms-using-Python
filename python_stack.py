"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementing the data-structure stack using python.
"""

class stack(object):

	def __init__(self):
		self.stack_content = []

	def push(self, item):
		self.stack_content.append(item)

	def pop(self):
		self.stack_content.pop()


q = stack()

q.push(10)
print(q.stack_content)

q.push(11)
print(q.stack_content)

q.push(12)
print(q.stack_content)

q.pop()
print(q.stack_content)