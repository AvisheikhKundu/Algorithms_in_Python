
def binarySearch(arr, l, r, x):
	while l <= r:

		mid = l + (r - l) // 2

		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1

	# If we reach here, then the element
	# was not present
	return -1


# Driver Code
if __name__ == '__main__':
	arr = [3, 4, 5, 6, 7, 8, 9, 10]
	x = 9

	# Function call
	result = binarySearch(arr, 0, len(arr)-1, x)
	if result != -1:
		print("Element is present at index", result)
	else:
		print("Element is not present in array")































# def binary_search(arr, target):
#     """
#     Binary search algorithm to find the position of the target element in the given sorted list.

#     Parameters:
#     arr (list): The sorted list to search through.
#     target: The element to find in the list.

#     Returns:
#     int: The index of the target element if found, otherwise -1.
#     """
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid  # Return the index where the target is found
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # Return -1 if target is not found in the array

# # Example usage
# input_str = input("Enter a sorted list of numbers separated by spaces: ")
# input_list = [int(x) for x in input_str.split()]

# # Prompt the user to enter the target
# target = int(input("Enter the target number to search for: "))

# result = binary_search(input_list, target)  # Assign the result of binary_search to 'result'

# if result != -1:
#     print(f"Target {target} found at index {result}")
# else:
#     print("Target not found in the array")
