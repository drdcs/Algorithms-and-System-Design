"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of 
abs(sum(Subset1) – sum(Subset2)) should be a given difference.

set = [3,1,2,3]
difference = 3
     s1     s2  diff
 3, 1, 2    3    3
 3,3       1,2   3
 1,2,3      3    3       

output = 3

s1 - s2 = diff
s1 + s2 = s
s1 = (diff+s)/2

"""

def NumberOfSubsetGivenDiff(array, diff):
     N = len(array)
     W = (sum(array) + diff) // 2
     DP = [[0 for x in range(W+1)] for j in range(N+1)]
     for i in range(N+1):
         DP[i][0] = 1
     
     for i in range(1, N+1):
         for j in range(1, W+1):
            if j < array[i-1]:
                 DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] + DP[i-1][j-array[i-1]]
     return DP[-1][-1]
 
if __name__ == '__main__':
    array = [3,1,2,3]
    diff = 3
    print(NumberOfSubsetGivenDiff(array, diff))