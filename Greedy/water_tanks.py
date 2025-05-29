def min_tanks(S):
    n = len(S)
    min_tanks = 0
    solution = list(S)
    for i in range(n):
        if S[i] == "H":
            if (i == 0 or solution[i-1] != "T"):
                if i + 1 < n and S[i+1] == "_":
                    min_tanks += 1
                    solution[i+1] = "T"
                elif i > 0 and S[i-1] == "_":
                    min_tanks += 1
                    solution[i-1] = "T"
                else:
                    return -1, S
    return min_tanks, "".join(solution)

def print_test_case(case):
    solution = min_tanks(case)
    print("Input:", case)
    print("Solution:", solution[1] if solution[0] >= 0 else "None")
    if solution[0] >= 0:
        print("Min. amount of tanks", solution[0])
    print()

# print_test_case("__H_H")
# print_test_case("H_H_H")
print_test_case("_H_H_H_H")
# print_test_case("HH_H")
# print_test_case("_H_H_")
# print_test_case("_____")