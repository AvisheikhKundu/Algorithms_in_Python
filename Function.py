
def sum_array(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        result = result + arr[i]
    return result


nums = [2, 3, 4, 5, 6]
answer = sum_array(nums)
print(answer)
