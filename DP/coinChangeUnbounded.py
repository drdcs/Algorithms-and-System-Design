"""
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

"""


def coinSubProblem(array, W, N):
    """
    array of coins..
    Weight(W) to be achieved.
    Number(N) of Coins..
    """
    # initialize the tabulation
    DP = [[0 for x in range(W+1)]for j in range(N+1)]
    # if there is no weights to achieve then always 1 possible way to exclude
    for i in range(N+1):
        DP[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j < array[i-1]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] + DP[i][j-array[i-1]]
    return DP[-1][-1]

if __name__ == '__main__':
    array = [1,2,3]
    W = 4
    N = len(array)
    print(coinSubProblem(array, W, N))

    array = [1,2,5]
    W = 5
    N = len(array)
    print(coinSubProblem(array, W, N))

    array = [1,2,5]
    W = 13
    N = len(array)
    print(coinSubProblem(array, W, N))

