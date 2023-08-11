def bubblesort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[65,45,66,85,100,32,123,654,8]
# print(len(arr))
bubblesort(arr)
print(arr)
