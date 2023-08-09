arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
a = [0] * n
j = n - 1

for i in range(len(arr)):
    a[j] = arr[i]
    j -= 1

for i in range(n):
    print(f"{a[i]}\t", end="")

# Output formatting
print()
