"""
	@script-author: Amandeep Singh Khanna
	@sript-description: Computing quartiles in python using the TI-83 calculator method.
"""

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

def compute_quartiles(input_array):
	
	output = {
		"q0" : min(input_array),
		"q1" : None,
		"q2" : median(input_array),
		"q3" : None,
		"q4" : max(input_array),
		"iqr": None,
		"lower_limit" : None,
		"upper_limit" : None
	}

	sorted_array = input_array.copy()
	sorted_array.sort()
	midpoint = len(input_array) // 2

	if len(input_array) % 2 == 0:
		lower_array = sorted_array[0:midpoint]
		upper_array = sorted_array[midpoint:]
		output["q1"] = median(lower_array)
		output["q3"] = median(upper_array)
	else:
		lower_array = sorted_array[0:midpoint]
		upper_array = sorted_array[midpoint+1:len(sorted_array)]
		output["q1"] = median(lower_array)
		output["q3"] = median(upper_array)

	output["iqr"] = output["q3"] - output["q1"]
	output["lower_limit"] = output["q1"] - (1.5 * output["iqr"])
	output["upper_limit"] = output["q3"] + (1.5 * output["iqr"])

	return output

if __name__ == "__main__":
	array_val = [3, 7, 8, 5, 12, 14, 21, 13, 18, 19]
	print(compute_quartiles(array_val))

