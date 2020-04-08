"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementation of basic logic gates in python.
"""

def not_gate(x):
	y = (x-1)**2
	return y

def and_gate(x1, x2):
	y = x1 * x2
	return y

def or_gate(x1, x2):
	y = (x1 + x2) - (x1 * x2)
	return y

def nand_gate(x1, x2):
	y = and_gate(x1, x2)
	y = not_gate(y)
	return y

def nor_gates(x1, x2):
	y = or_gate(x1, x2)
	y = not_gate(y)
	return y

if __name__ == "__main__":
	print("not_gate outputs:")
	# Expected output - 1
	print(not_gate(0)) 
	# Expected output - 0
	print(not_gate(1))

	print("and_gate outputs:")
	# Expected output:
	# 0
	# 0
	# 0
	# 1

	print(and_gate(0, 0))
	print(and_gate(1, 0))
	print(and_gate(0, 1))
	print(and_gate(1, 1))

	print("or_gate outputs:")
	# Expected output:
	# 0
	# 1
	# 1
	# 1

	print(or_gate(0, 0))
	print(or_gate(1, 0))
	print(or_gate(0, 1))
	print(or_gate(1, 1))