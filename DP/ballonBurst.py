"""
Burst Balloon to maximize coins
 
We have been given N balloons, each with a number of coins associated with it. On bursting a balloon i, 
the number of coins gained is equal to A[i-1]*A[i]*A[i+1]. Also, balloons i-1 and i+1 now become adjacent. 
Find the maximum possible profit earned after bursting all the balloons. Assume an extra 1 at each boundary.
Examples: 

Input : 5, 10
Output : 60
Explanation - First Burst 5, Coins = 1*5*10
              Then burst 10, Coins+= 1*10*1
              Total = 60

Input : 1, 2, 3, 4, 5
Output : 110

"""

def getMax(A): 
    N = len(A) 
    A = [1] + A + [1]# Add Bordering Balloons 
    dp = [[0 for x in range(N + 2)] for y in range(N + 2)]# Declare DP Array 
      
    for length in range(1, N + 1): 
        for left in range(1, N-length + 2): 
            right = left + length -1
  
            # For a sub-array from indices left, right 
            # This innermost loop finds the last balloon burst 
            for last in range(left, right + 1): 
                dp[left][right] = max(dp[left][right], \
                                      dp[left][last-1] + \
                                      A[left-1]*A[last]*A[right + 1] + \
                                      dp[last + 1][right]) 
    return(dp[1][N]) 
  
# Driver code 
A = [1, 2, 3, 4, 5] 
print(getMax(A)) 
