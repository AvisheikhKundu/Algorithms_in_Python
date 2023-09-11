def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i +=1
    arr[i], arr[high] = arr[high], arr[i]
    return i
def quicksort(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

a = [20, 15, 4, 69,3, 4.55, 5.55]
quicksort(a, 0, len(a)-1)
print(a)
