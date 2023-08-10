arr = [1, 2, 3, 4, 5, 6]
x = len(arr)
a = [0] * x
j = x - 1

for i in range(len(arr)):
    a[j] = arr[i]
    j -= 1

for i in range(x):
    print(f"{a[i]}\t", end="")

print()
