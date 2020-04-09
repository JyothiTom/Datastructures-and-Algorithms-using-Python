"""
	@script-author: Amandeep Singh Khanna
	@script-description: Computing pearson's correlation coefficent using python.
"""

# pearsons_r = cov(x,y)/ (std(x)*std(y))
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
	numerator = [(x-average_x)*(y-average_y) for x, y in zip(x_array, y_array)]
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

if __name__ == "__main__":
	x = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
	y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
	print(compute_pearsons_correlation(x, y))