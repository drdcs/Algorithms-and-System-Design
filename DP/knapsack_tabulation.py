# Explanation : https://www.youtube.com/watch?v=WNkqbqyvR_0
# Code reference : https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack_tabulation(weight, profit, W, N):
    K = [[-1 for x in range(W+1)] for j in range(N+1)]
    for i in range(N+1):
        for w in range(W+1):
            # base case
            if i == 0  or w == 0:
                K[i][w] = 0
            # skip case
            elif weight[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w] , 
                            profit[i-1]+ K[i-1][w- weight[i-1]])
    return K[N][W]

if __name__ == '__main__':
    Weight = [1, 2, 3, 4, 5]
    Profit = [3, 4, 5, 2, 1]
    W = 6
    N = len(Weight)
    print(knapsack_tabulation(Weight, Profit, W, N))       
            