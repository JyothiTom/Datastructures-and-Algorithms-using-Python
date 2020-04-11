"""
	@script-author: Amandeep Singh Khanna
	@script-description: Python code to compute fibonacci sequence using a for loop.
"""

# Fibonacci sequence using the for loop:
def fibonacci_forloop(n):
	if n>=0: # If n is negative
		if n==0: # If n is zero
			return 0
		else: # If n is greater than zero
			sequence = [0, 1]
			last_val = 0
			next_val = 1
			for _ in range(1, n):
				temp_val = last_val + next_val
				last_val = next_val
				next_val = temp_val
				sequence.append(next_val)
			return sequence
	else:
		"n must be 0 or a positive integer"

# 0, 1, 1, 2, 3, 5, 8 - expected output
print(fibonacci_forloop(6))