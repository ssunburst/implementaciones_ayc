def matrix_multiplication(P):
    n = len(P) - 1
    M = []
    S = []
    for i in range(n):
        M.append([float('inf')] * n)
        S.append([float('inf')] * n)
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                M[i][j] = 0
                S[i][j] = -1
            else:
                for k in range(i, j):
                    local_cost = M[i][k] + M[k+1][j] + P[i]*P[k+1]*P[j+1]
                    if local_cost < M[i][j]:
                        M[i][j] = local_cost
                        S[i][j] = k
    return M[0][n-1], parenthize(S, n)

def parenthize(S, n):
    return _parenthize_recursive(0, n-1, S)

def _parenthize_recursive(i, j, S):
    if i < j:
        k = S[i][j]
        return f"({_parenthize_recursive(i, k, S)} {_parenthize_recursive(k+1, j, S)})"
    else:
        return f"{i + 1}"


if __name__ == "__main__":
    print(matrix_multiplication([30, 35, 15, 5, 10, 20, 25]))
