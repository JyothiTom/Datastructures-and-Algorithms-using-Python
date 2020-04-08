"""
	@script-author: Amandeep Singh Khanna
	@script-description: Computing the standard deviation using python
"""
import math

def standard_deviation(input_array, std_type="population"):
	sample_val = 0
	if std_type == "sample":
		sample_val = 1
	average_val = sum(input_array)/len(input_array)
	deviations = [(x-average_val)**2 for x in input_array]
	standard_deviation_val = math.sqrt(sum(deviations)/(len(input_array)-sample_val))
	return standard_deviation_val

if __name__ == "__main__":
	array_val = [10, 40, 30, 50, 20]
	print(standard_deviation(array_val, "population"))
	print(standard_deviation(array_val, "sample"))