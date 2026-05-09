import math

def solution(A):
    
    def solution_aux(A, start, end):
        if start == end:
            return A[start], start, end
        else:
            mid = (start + end) // 2

            west_sum, west_start, west_end = solution_aux(A, start, mid)
            east_sum, east_start, east_end = solution_aux(A, mid+1, end)
            cross_sum, cross_start, cross_end = find_cross_sum(A, start, end)
    
            sum_start = west_start if west_sum >= east_sum else east_start
            sum_end = west_end if west_sum >= east_sum else east_end
            sum = west_sum if west_sum >= east_sum else east_sum 

            if west_sum > east_sum:
                sum_start = west_start
                sum_end = west_end
                sum = west_sum
            else:
                sum_start = east_start
                sum_end = east_end
                sum = east_sum

            if cross_sum > sum:
                sum_start = cross_start
                sum_end = cross_end
                sum = cross_sum
            
            return sum, sum_start, sum_end
        
    def find_cross_sum(A, start, end):
        mid = (start + end) // 2
        current_sum = 0
        sum_start, west_sum = mid, -math.inf
        for i in range(sum_start, start - 1, -1):
            current_sum += A[i]
            if current_sum > west_sum:
                sum_start = i
                west_sum = current_sum
        current_sum = 0
        sum_end, east_sum = mid + 1, -math.inf
        for i in range(sum_end, end + 1):
            current_sum += A[i]
            if current_sum > east_sum:
                sum_end = i
                east_sum = current_sum
        return west_sum + east_sum, sum_start, sum_end
    
    n = len(A)
    return solution_aux(A, 0, n-1)

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
sol = solution(A)
print("Input: ", A)
print("\nMaximum sum subarray found to amount to", sol[0] ,"from index", sol[1]+1, "to index", sol[2]+1, "(indexing 1..n).")
print(A[sol[1]:(sol[2]+1)])



