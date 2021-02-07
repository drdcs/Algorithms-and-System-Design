"""
Given two arrays arr1[] and arr2[] each of size N.
The task is to choose some elements from both the arrays such that no two elements have the same index and no two consecutive numbers can be selected from a single array. Find the maximum sum possible of above-chosen numbers.

arr1 = [9,3,5,7,3]
arr2 = [5,8,1,4,5]

"""

def max_sum(arr1, arr2, n):
    dp = [[0 for i in range(2)] for j in range(n)]

    dp[0][0] = arr1[0]
    dp[1][0] = arr2[0]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+arr1[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + arr2[i])

    return dp #max(dp[n-1][0], dp[n-1][1])

if __name__ == '__main__':
    arr1 = [9,3,5,7,3]
    arr2 = [5,8,1,4,5]
    print(max_sum(arr1, arr2, len(arr1)))