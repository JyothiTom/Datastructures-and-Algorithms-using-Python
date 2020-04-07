"""
	@script-author: Amandeep Singh Khanna
	@script-description: Implementing linear search using python
"""

def linear_search(input_array, search_element):
	if len(input_array) > 0:
		if search_element not in input_array:
			return f"The element {search_element} is not in the input array {input_array}"

		for index_position in range(len(input_array)):
			if search_element == input_array[index_position]:
				return f"The search_element {search_element} found at the position {index_position} in the input_array"
	else:
		return "The search array is empty"

array_val = [10, 11, 23, 1, 289, 2345, 345, 0]

print(linear_search(input_array = array_val, search_element = 0))