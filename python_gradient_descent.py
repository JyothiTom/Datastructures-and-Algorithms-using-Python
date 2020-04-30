"""
    @script-author: Amandeep Singh Khanna
    @script-description: Implementation of gradient descent algorithm using python.
"""

# function:
# f(x) = 4x^3 + x^2 - 2x + 1
# f!(x) = 12x2 + 2x - 2 + 0

# setting the important parameters for gradient descent:

def derivative(x):
    return 12 * x**2 + 2 * x - 2

current_val = 6 # the first value in the gradient.
iter_val = 1000 # number of times there should be a small change.
learning_rate = 0.001 # the step size.

changes = []

for _ in range(iter_val):
    next_val = current_val - learning_rate * derivative(current_val)
    changes.append(current_val)
    print(current_val)
    current_val = next_val