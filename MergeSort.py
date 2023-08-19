def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    sortedleft = mergesort(left)
    sortedright = mergesort(right)
    i, j = 0, 0
    sortedarr = []
    while(i < len(sortedleft)) and j < len(sortedright):
        if sortedleft[i] < sortedright[j]:
            sortedarr.append(sortedleft[i])
            i += 1
        else:
            sortedarr.append(sortedright[j])
            j += 1

    return sortedarr + sortedleft[i:] + sortedright[j:]
a = [2, 8, 3, 5]
print (mergesort(a))
