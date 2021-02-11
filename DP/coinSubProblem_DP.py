"""
set[]={3, 4, 5, 2}
target=6
 
  |  0    1    2    3    4    5    6 COINS 
-------------------------------------
0 |  T    F    F    F    F    F    F
-------------------------------------
3 |  T    F    F    T    F    F    F
-------------------------------------     
4 |  T    F    F    T    T    F    F   
-------------------------------------     
5 |  T    F    F    T    T    T    F
-------------------------------------
2 |  T    F    T    T    T    T    T
-------------------------------------
"""

def coinExchange(coins, W, N):

    # build the 2-d array.
    K = [[False for i in range(W+1)]  for j in range(N+1)]
    # if there is no weight we can exchange it with no coin.
    # because there are only 2 possibility of a coin either include or exclude.
    for i in range(N+1):
        K[i][0] = True
    
    # Fill the table in bottom up manner.
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j < coins[i-1]:
                K[i][j] = K[i-1][j]
            if j >= coins[i-1]:
                K[i][j] = (K[i-1][j] or K[i-1][j-coins[i-1]])
    
    return K[-1][-1]
    
if __name__ == '__main__':

    coins = [1, 6, 7, 8]
    W = 1
    N = len(coins)

    TF = coinExchange(coins, W, N)
    print(TF)