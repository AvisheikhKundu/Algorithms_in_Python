def FirstFit(products, target):
    res =  0
    products.sort(reverse=True)
    bin_rem = [0]*len(products)

    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j] >= p:
                bin_rem[j] = bin_rem[j]-p
                break
            j+=1
        if (j==res):
            bin_rem[res] = target - p
            res += 1
    return res

products =[6,3,2,4,1,5]
target = 7
print("Minimum packets:", FirstFit(products, target))
