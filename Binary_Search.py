def binary_search(numbers,number_to_find):
    low=0
    high=len(numbers)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(numbers[mid]==number_to_find):
            return mid
        elif (numbers[mid]<number_to_find):
            low=mid+1
        else :
            high=mid-1
    return -1
a=list(map(int, input("elements of array:-").strip().split()))
n=int(input())
if (binary_search(a,n)==-1):
    print("Not found")
else :
    print("Found in index",str(binary_search(a,n)))


#AN_EXAMPLE:

    def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
