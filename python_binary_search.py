"""
    @script-author: Amandeep Singh Khanna
    @script-description: Implementing binary search using python
"""

def binarysearch(input_array, search_element, sort_array = False):
    
    if len(input_array) == 0:
        return "input_array is empty"

    if search_element not in input_array:
        return f"search_element {search_element} not found in the input_array"

    if sort_array == True:
        input_array.sort()
        print(f"The array is sorted:\n{input_array}")

    first = 0
    last  = len(input_array)-1

    while first < last:

        middle = first + (last - first) // 2 # floor division
        print(f"first {first} - middle {middle} - last {last}")

        if search_element == input_array[middle]:
            return f"search_element {search_element} found at position {middle}"

        elif search_element > input_array[middle]:
            first = middle

        else:
            last = middle

array = [10,1,20,23,234,25,32,129,237]

print(binarysearch(input_array=array, search_element=129, sort_array=True))

print(binarysearch(input_array=array, search_element=10, sort_array=True))