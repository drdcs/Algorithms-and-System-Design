def countSubset(array, W, N):
    DP =[[-1 for x in range(W+1)] for j in range(N+1)]
    # base case
    if W == 0:
        return 1
    if N == 0:
        return 0
    if DP[N][W] != -1:
        return DP[N][W]

    if array[N-1] > W:
        DP[N][W] =  countSubset(array, W, N-1)
        return DP[N][W]
    else:
        DP[N][W] = countSubset(array, W, N-1) + countSubset(array, W - array[N-1], N-1)
        return DP[N][W]
        
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    W = 7
    N = len(array)
    print(countSubset(array, W, N))