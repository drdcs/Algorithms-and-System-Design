"""
ref: https://www.youtube.com/watch?v=ZI17bgz07EE&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=14
we have infinite supply of coins , we need to achieve change with
minimum number of coins.

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

"""

"""
Build the tabulation 
array = [1,2,5]
Amt = 6

        0 1 2 3 4 5 6 weight 
    - - - - - - - - - - -
     0| 0 I I I I I I
     1| 0 1 2 3 4 5 6 
     2| 0 1 1 2 2 3 3
     3| 0 1 1 2 2 1 2
     
"""

def minCoinExchange(array, W):
    N = len(array)
    # DP table will be storing the minimum number
    # of coins required.      
    DP = [[0 for x in range(W+1)] for j in range(N+1)]
    for i in range(N+1):
        DP[i][0] = 0
    for j in range(1,W+1):
        DP[0][j] = float('inf')
    for i in range(1, N+1):
        for j in range(1, W+1):
            # if weight is less than the number we need to exclude.
            if j < array[i-1]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = min(DP[i-1][j], (1 + DP[i][j-array[i-1]]))
    return DP[-1][-1]

if __name__ == '__main__':
    coins = [1,2,5]
    v = 6
    print(minCoinExchange(coins, v))
