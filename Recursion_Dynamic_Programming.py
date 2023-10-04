def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return f(n-1) + f(n-2)

print(f(5))

def fn(n):
    l = [0,1]
    k = 2
    for i in range(k,n):
        l.append(l[i-1]+l[i-2])
        return l[-1]
