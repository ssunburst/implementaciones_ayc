def max_score(V):
    n = len(V)
    scores = []
    moves = []
    
    for i in range(n):
        scores.append([0] * n)
        moves.append([0] * n)
    
    for i in range(n - 1, -1, -1):  # i from n-1 downto 0
        for j in range(i, n):       # j from i to n-1
            if i == j:
                scores[i][j] = V[i]
                moves[i][j] = i
            else:
                if V[i] - scores[i+1][j] >= V[j] - scores[i][j-1]:
                    scores[i][j] = V[i]
                    moves[i][j] = i
                else:
                    scores[i][j] = V[j]
                    moves[i][j] = j

    move_sequence = reconstruct_moves(V, moves)
    return scores[0][n-1], move_sequence

def reconstruct_moves(V, M):
    moves = []
    n = len(V)
    i = 0
    j = n -1
    turn = True
    while i != j:
        if M[i][j] == i:
            if turn:
                moves.append(V[i])
            i += 1
        else:
            if turn:
                moves.append(V[j])
            j -= 1
        turn = not turn
    if turn:
        moves.append(V[i])
    return moves

if __name__ == "__main__":
    print(max_score([2, 5, 3, 3, 8]))