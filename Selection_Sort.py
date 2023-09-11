def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    # Input: You can take a list of numbers from the user
    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]

    selection_sort(input_list)

    # Output: Sorted list
    print("Sorted list:", input_list)
