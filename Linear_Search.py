def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if target is not found in the array

# Example usage
arr = [3, 9, 4, 2, 7, 1]
target = 7
result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array")
