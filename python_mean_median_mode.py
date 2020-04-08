"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementation of mean, median and mode using python.
"""

def mean(input_array):
	mean_value = sum(input_array)/len(input_array)
	return mean_value

def median(input_array):
	sorted_array = input_array.copy()
	sorted_array.sort()
	midpoint = len(input_array) // 2
	print(sorted_array)
	if len(input_array) % 2 == 0:
		median = (sorted_array[midpoint-1] + sorted_array[midpoint])/2
	else:
		median = sorted_array[midpoint] 
	return median

def mode(input_array):
	element_counts = {index_val:0 for index_val in input_array }
	for array_element in input_array:
		element_counts[array_element] += 1
	modal_freq = max(element_counts.values())
	mode = [key for key, value in element_counts.items() if value == modal_freq]
	return mode

if __name__ == "__main__":
	array_val = [10, 22, 1, 232, 453, 567, 98, 2, 12, 12, 13]
	print(mean(array_val))
	print(mode(array_val))
	print(median(array_val))
