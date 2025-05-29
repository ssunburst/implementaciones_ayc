def min_difference(A, n):
    A.sort()
    min_difference = float('inf')
    for i in range(len(A) - n + 1):
        min_difference = min(min_difference, A[i + n - 1] - A[i])
    return min_difference

print(min_difference([10, 12, 90, 7, 5, 22], 4))


