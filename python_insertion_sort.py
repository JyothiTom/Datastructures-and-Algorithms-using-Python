"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementation of insertion sort in python.
"""
def insertion(input_array, arr_index):
	for index_val in range(arr_index, 0, -1):
		if input_array[index_val] < input_array[index_val-1]:
			temp = input_array[index_val]
			input_array[index_val] = input_array[index_val-1]
			input_array[index_val-1] = temp

def insertionsort(input_array):
	if len(input_array)>0:
		for arr_index in range(1, len(input_array)):
			insertion(input_array, arr_index)
		return input_array
	else:
		return "input_array is empty"

if __name__ == "__main__":
	array_val = [102, 0, 232,23,1,5,67,3,92,1]
	print(insertionsort(array_val))
