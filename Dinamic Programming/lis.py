def lis(S):
    n = len(S)
    LIS = [1] * n
    max_length = LIS[n-1]
    max_index = n - 1
    next = [-1] * n
    for i in range(n-2, -1, -1):
        for j in range(i + 1, n):
            if S[j] > S[i]:
                if LIS[j] + 1 > LIS[i]:
                    next[i] = j
                    LIS[i] = 1 + LIS[j]
        if (LIS[i] > max_length):
            max_length = LIS[i]
            max_index = i
    return (max_length, max_index, next)

def reconstruct_sequence(S, max, next):
    sequence = [S[max]]
    i = max
    while next[i] != -1:
        sequence.append(S[next[i]])
        i = next[i]
    return sequence


if __name__ == "__main__":
    S = [4, 5, 2, 1, 3, 4, 12, 1, 9]
    results = lis(S)
    longest_sequence = reconstruct_sequence(S, results[1], results[2])
    print("La subsecuencia creciente más larga del arreglo", S, "tiene largo", results[0], "y es", longest_sequence)