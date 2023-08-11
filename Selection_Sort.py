def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(unsorted_list)
    print("Sorted List:", unsorted_list)
