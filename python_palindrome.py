"""
	@script-author: Amandeep Singh Khanna
	@script-description: Python code to check if a string is a palindrome or not
"""
def palindrome_check(input_word):
	if len(input_word)>0:
		reversed_word = input_word[::-1]
		if input_word == reversed_word:
			return f"{input_word} is a palindrome"
		else:
			return f"{input_word} is not a palindrome"

if __name__ == '__main__':
	# palindrome detected - expected output
	print(palindrome_check("dad"))
	# not a palindrome - expected output
	print(palindrome_check("dollar"))