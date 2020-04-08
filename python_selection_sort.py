"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementation of selection sort using python.
"""

def compute_min_index(input_array, input_index):
	minimum_pos = input_index
	for index_val in range(input_index, len(input_array)):
		if input_array[index_val] < input_array[minimum_pos]:
			minimum_pos = index_val
	return minimum_pos

def selection_sort(input_array):
	for index_val in range(len(input_array)-1):
		minimum_pos = compute_min_index(input_array, index_val)
		if minimum_pos != index_val:
			temp = input_array[minimum_pos]
			input_array[minimum_pos] = input_array[index_val]
			input_array[index_val] = temp
	return input_array


if __name__ =="__main__": 
	# [0, 1, 2, 9, 14, 43, 45, 78, 232, 431] - Expected output
	array_val =  [1, 232, 43, 431, 9 , 0, 2, 45, 78, 14]
	print(selection_sort(array_val))