def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]

# Call the bubble_sort function to sort the input list
bubble_sort(input_list)

# Print the sorted list
print("Sorted list:", input_list)
