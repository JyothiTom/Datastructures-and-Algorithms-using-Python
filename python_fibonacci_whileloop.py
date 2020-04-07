"""
	@script-author: Amandeep Singh Khanna
	@script-description: Python code to compute fibonacci sequence using a while loop.
"""

# Fibonacci sequence using the while loop:
def fibonacci_while(n):
	if n>=0: # If n is negative
		if n==0: # If n is zero
			return 0
		else: # If n is greater than zero
			sequence = [0, 1]
			while len(sequence) < n:
				x = sequence[(len(sequence)-1)]
				y = sequence[(len(sequence) - 2)]
				sequence.append(x+y)
			return sequence
	else:
		return "n must be 0 or a positive integer"

# 0, 1, 1, 2, 3, 5 - expected output
print(fibonacci_while(6))

