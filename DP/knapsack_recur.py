# Weight = [1, 2, 3, 4, 5]
# Profit = [3, 4, 5, 2, 1]
# W = 6
# N = 5 - 1 = 4
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# Time Complexity: O(2n). 
# As there are redundant subproblems.
# Auxiliary Space :O(1). 

def maxProfitKnapSack(Weight, Profit, W, N):
    # base condition
    if(N==0 or W == 0):
        return 0
    
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution 

    if (Weight[N-1] > W):
        return maxProfitKnapSack(Weight, Profit, W, N-1)

    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 

    else:
        return max(maxProfitKnapSack(Weight, Profit, W, N-1), 
           Profit[N-1] + maxProfitKnapSack(Weight, Profit, W - Weight[N-1], N-1))

if __name__ == '__main__':
    Weight = [1, 2, 3, 4, 5]
    Profit = [3, 4, 5, 2, 1]
    W = 6
    N = len(Weight)
    print(maxProfitKnapSack(Weight, Profit, W, N))