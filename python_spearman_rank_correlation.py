"""
	@script-author: Amandeep Singh Khanna
	@script-description: Computing Spearman's rank correlation coefficient. 
"""

import math

def standard_deviation(input_array, population=True):
	sample_val = 0

	if population == False:
		sample_val = 1

	average_val = sum(input_array)/len(input_array)
	deviations = [(x-average_val)**2 for x in input_array]
	standard_deviation_val = math.sqrt(sum(deviations)/(len(input_array)-sample_val))
	return standard_deviation_val

def covariance(x_array, y_array, population=True):
	average_x = sum(x_array)/len(x_array)
	average_y = sum(y_array)/len(y_array)
	numerator = [(x-average_x)*(y-average_y) for x, y in zip(x_array, y_array)] # zip function
	numerator = sum(numerator)
	sample_val = 0
	
	if population == False:
		sample_val = 1
	
	covariance = numerator/(len(x_array)-sample_val)
	return covariance

def compute_pearsons_correlation(x_array, y_array):
	if len(x_array) == len(y_array):
		covariance_val = covariance(x_array, y_array)
		print(f"covariance: {covariance_val}")
		sd_x = standard_deviation(x_array)
		sd_y = standard_deviation(y_array)
		r = covariance_val/(sd_x*sd_y)
		return r
	else:
		return "x_array and y_array are not of equal lenghts"

def generate_ranks(input_array):
	sorted_array = input_array.copy()
	sorted_array.sort()
	ranks = {}
	counter = 0
	duplicate_flag = False
	for index_val in range(len(input_array)):
		if sorted_array[index_val] not in ranks.keys():
			counter += 1
			ranks[sorted_array[index_val]] = counter
		else: 
			duplicate_flag = True
	rank = [ranks[i] for i in input_array]
	return rank, duplicate_flag

def compute_correlation(x_array, y_array):
	if len(x_array) == len(y_array):
		x_rank, x_duplicate_flag = generate_ranks(x_array)
		y_rank, y_duplicate_flag = generate_ranks(y_array)
		if x_duplicate_flag == True or y_duplicate_flag == True: # If n ranks are not distinct
			correlation_coefficent = compute_pearsons_correlation(x_rank, y_rank)
			return correlation_coefficent
		else: # distinct ranks
			d_array = [(x-y)**2 for x, y in zip(x_rank, y_rank)]
			d = sum(d_array)
			correlation_coefficent = 1 - ((6*d)/(len(x_array)*(len(x_array)**2 - 1)))
			return correlation_coefficent
	else:
		return "x_array and y_array should have the same length"

if __name__ == "__main__":
	x = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
	y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
	print(compute_correlation(x, y))