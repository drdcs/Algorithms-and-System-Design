# O(N*W) | O(N*W)

def knapsack_dp(weight, profit, W, n):
    
    Matrix =[[-1 for x in range(W+1)] for j in range(n+1)]
    # base case
    if (n == 0 or W == 0):
        return 0
    
    if Matrix[n][W] != -1:
        return Matrix[n][W]
            
    if weight[n-1] > W:
        Matrix[n][W] = knapsack_dp(weight, profit, W, n-1)
        return Matrix[n][W]
    else:
        Matrix[n][W] = max(knapsack_dp(weight, profit, W, n-1), 
        profit[n-1]+ knapsack_dp(weight, profit, W - weight[n-1], n-1))
        return Matrix[n][W]
if __name__ == '__main__':
    Weight = [1, 2, 3, 4, 5]
    Profit = [3, 4, 5, 2, 1]
    W = 6
    N = len(Weight)
    print(knapsack_dp(Weight, Profit, W, N))
