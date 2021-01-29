"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11    

idea : proceed with knapsack problem and take the last row
for which the value is True. and find the minimum difference 
created.

"""

def diffSubSet(array, W, N):
    matrix = [[False for x in range(W+1)] for y in range(N+1)]
    for i in range(N+1):
        matrix[i][0] = True
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j > array[i-1]:
                matrix[i][j] = matrix[i-1][j]

            else:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j - array[i-1]]
    
    diff = float("inf")
    for j in range(W//2, -1, -1):
        if matrix[N][j] == True:
            diff = W - (2 * j)
            break
    return diff


if __name__ == '__main__':

    array = [1, 6, 11, 5]
    W = sum(array)
    N = len(array)
    print(diffSubSet(array, W, N))

