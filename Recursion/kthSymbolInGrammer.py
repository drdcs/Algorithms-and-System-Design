"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row 
and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. 
(The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

"""

# Observations  --- 

'''
N = 1 => 0
N = 2 => 0 | 1
N = 3 => 0 1 | 1 0
N = 4 => 0 1 1 0 | 1 0 0 1

** Every row has pow(2, n-1) elements . 
** After mid the bits are complementing.
** before mid it's the same element of n-1th row

'''

def solve(n, k):
    # base condition
    if n == 1 and k == 1:
        return 0

    mid = pow(2, n-1) // 2

    if k <= mid:
        return solve(n-1, k)
    else:
        return 1 - solve(n-1, k-mid)

if __name__ == '__main__':
    print(solve(2,2))
