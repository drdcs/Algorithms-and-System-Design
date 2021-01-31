"""

rod has 2 properties , weight and price

# Not sure , needs correction

"""

def rodCutting(price, W, N):

    DP = [[0 for x in range(W+1)] for j in range(N+1)]
    
    for i in range(0, N+1):
        DP[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j < price[i-1]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j],price[i-1]+DP[i][j-price[i-1]])
    return DP

if __name__ == '__main__':
    # array = [1, 5, 8, 9]
    # N = len(array)
    # W = 9
    # print(rodCutting(array, W, N))

    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    W = 20
    print(rodCutting(arr,W,size))