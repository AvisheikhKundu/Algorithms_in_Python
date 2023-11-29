def findMin(V):

	deno = [1, 2, 5, 10, 20, 50,
			100, 500, 1000]
	n = len(deno)

	# Initialize Result
	ans = []

	# Traverse through all denomination
	i = n - 1
	while(i >= 0):

		# Find denominations
		while (V >= deno[i]):
			V -= deno[i]
			ans.append(deno[i])

		i -= 1

	# Print result
	for i in range(len(ans)):
		print(ans[i], end = " ")

# Driver Code
if __name__ == '__main__':
	n = 170
	print("Following is minimal number",
		"of change for", n, ": ", end = "")
	findMin(n)
