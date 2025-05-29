def longest_common_subsequence(X, Y):
    subsequences = []
    m = len(X); n = len(Y)
    for i in range(m):
        subsequences.append([0] * n)
    for i in range(0, m):
        for j in range(0, n):
            if (X[i] == Y[j]):
                subsequences[i][j] = subsequences[i-1][j-1] + 1 if (i > 0 and j > 0) else 1
            else:
                prev_row = subsequences[i-1][j] if i > 0 else 0
                prev_column = subsequences[i][j-1] if j > 0 else 0
                subsequences[i][j] = max(prev_row, prev_column)
    return subsequences[m - 1][n - 1]

if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    expected_length = len("BCBA")
    print("Expected length:", expected_length, "- Obtained length:", longest_common_subsequence(X, Y))
