def NextFit(products, target):
    res = 1
    c = target
    for p in products:
        if target - p >= 0:
            target = target - p
        else:
            res += 1
            target = c - p
    return res

products = [6,3,2,4,1,5]
target = 7
print("'Minimum Packets: ", NextFit(products, target))
