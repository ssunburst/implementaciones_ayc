import numpy as np

p = 2
w = 1

def max_score(A, B):
    n = len(A)
    scores = []
    for i in range(0, n + 1):
        scores.append([0] * (n+1))
    scores[n][n] = 0
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if i == n and j == n:
                scores[i][j] = 0
            elif j == n:
                scores[i][j] = scores[i+1][j] - p
            elif i == n:
                scores[i][j] = scores[i][j+1] - p
            else:
                score = max(scores[i+1][j], scores[i][j+1]) - p
                bonus = 1 if A[i] == B[j] else -w
                score = max(score, scores[i+1][j+1] + bonus)
                scores[i][j] = score
    return scores[0][0]

A = "EAKKLNDAQAPKDN"
B = "EAKSDEAEALKSDE"

print(max_score(A, B))
            