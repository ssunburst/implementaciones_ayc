def combine_horizons(H1, H2):
    n = len(H1)
    m = len(H2)
    i = j = 0
    H = []
    current_height = H1_height = H2_height = 0
    while (i < min(n,m)) and (j < min(n, m)):
        H1_height = H1_height if H1[i] > H2[j] else H1[i+1]
        H2_height = H2_height if H2[j] > H1[i] else H2[j+1]
        candidate_height = max(H1_height, H2_height)
        if candidate_height != current_height:
            H.append(min(H1[i], H2[j]))
            H.append(candidate_height)
            current_height = candidate_height
        if H1[i] <= H2[j]:
            i += 2
        elif H2[j] <= H1[i]:
            j += 2
    while i < n:
        H.append(H1[i])
        i += 1
    while j < m:
        H.append(H2[j])
        j += 1
    return H

def horizon(T):
    n = len(T)
    if n == 1:
        return list(T[0]) + [0]
    else:
        H1 = horizon(T[:(n // 2)])
        H2 = horizon(T[(n // 2):])
        return combine_horizons(H1, H2)
    
if __name__ == "__main__":
    print(horizon([
        (5, 7, 14),
        (8, 18, 12),
        (11, 16, 14),
        (13, 10, 18),
        (16, 23, 21),
        (20, 8, 23),
        (22, 4, 25),
        (25, 2, 30),
        (30, 12, 36),
        (41, 11, 46),
        (44, 6, 50)
    ]))

