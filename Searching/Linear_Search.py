def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if target is not found in the array

# Example usage
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]

# Prompt the user to enter the target
target = int(input("Enter the target number to search for: "))

result = linear_search(input_list, target)  # Assign the result of linear_search to 'result'

# Output: Sorted list
print("Sorted list:", input_list)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array")
