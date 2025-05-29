def find_maximum_subarray(A):
    return _find_maximum_subarray_aux(A, 0, len(A) - 1)

def _find_maximum_subarray_aux(A, i, j):
    if i == j:
        return (i, i, A[i])
    else:
        mid = (i + j) // 2
        left_low, left_high, left_sum = _find_maximum_subarray_aux(A, i, mid)
        right_low, right_high, right_sum = _find_maximum_subarray_aux(A, mid + 1, j)
        cross_low, cross_high, cross_sum = _find_maximum_crossing_subarray(A, i, mid, j)
        low, high, sum = (left_low, left_high, left_sum) if left_sum > right_sum else (right_low, right_high, right_sum)
        low, high, sum = (low, high, sum) if sum > cross_sum else (cross_low, cross_high, cross_sum)
        return (low, high, sum)

def _find_maximum_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

if __name__ == '__main__':
    print(find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
