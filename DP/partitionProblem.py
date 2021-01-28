"""
Partition problem is to determine whether a given set
can be partitioned into two subsets such that the sum of 
elements in both subsets is the same. 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

"""

'''

There are 2 important observation.
(obj 1) - If sum of the array is Odd , we can't divide this into
          2 subsets. Mathematically 
            (odd + odd) = even
            (even + even) = even
(obj 2) - so, if we take the sum and divide this by 2 (W) and figure out
         if the sum is possible or not then it is a 0/1 knapsack problem.

'''


def PartitionProblem(array):
    W = sum(array)
    if (W % 2) == 1:
        return False
    else:
        W = W // 2
        N = len(array)

        K = [[False for x in range(W+1)] for j in range(N+1)]
        
        for i in range(N+1):
            K[i][0] = True
        
        for i in range(1, N+1):
            for j in range(1, W+1):
                if j < array[i-1]:
                    K[i][j] = K[i-1][j]
                if j >= array[i-1]:
                    K[i][j] = (K[i-1][j] or K[i-1][j - array[i-1]])
    return K[-1][-1]
                    
if __name__ == '__main__':
    array = [3, 1, 5, 9, 12]
    print(PartitionProblem(array))
