#ATTEMPT 1

# Python 3 program to find no. of ways
# to fill a 3xn board with 2x1 dominoes.

def countWays(n):

	A = [0] * (n + 1)
	B = [0] * (n + 1)
	A[0] = 1
	A[1] = 0
	B[0] = 0
	B[1] = 1
	for i in range(2, n+1):
		A[i] = A[i - 2] + 2 * B[i - 1]
		B[i] = A[i - 1] + B[i - 2]
	
	return A[n]

n = 8
print(countWays(n))

# This code is contributed by Smitha

