def max_sum(A):
    max_sum = currentMax = A[-1]
    for i in range(len(A)-2, -1, -1):
        currentMax = max(A[i], A[i] + currentMax)
        max_sum = max(currentMax, max_sum)
    return max_sum

A = [3, -4, 5, -2, -2, 6, -3, 5, -3, 2]
print(max_sum(A))