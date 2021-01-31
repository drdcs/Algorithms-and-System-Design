"""
Given a rod of length n inches and an array of prices that contains 
prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod 
and selling the pieces. 
For example, if length of the rod is 8 
and the values of different pieces are given as following, 
then the maximum obtainable value is 22 
(by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

1) Optimal Substructure: 
We can get the best price by making a cut at different positions and comparing the values obtained after a cut. We can recursively call the same function for a piece obtained after a cut.
Let cutRod(n) be the required (best possible price) value for a rod of length n. cutRod(n) can be written as following.
cutRod(n) = max(price[i] + cutRod(n-i-1)) for all i in {0, 1 .. n-1}

"""


def cuttingRod(price, N):
    if N <= 0:
        return 0
    maxVal = float('-inf')
    for i in range(0,N):
        maxVal =  max(maxVal, price[i] 
        + cuttingRod(price, N-i-1))
    return maxVal
    
"""
If we build the recusrsive structure we can see that the value been reevaluating
again and again. if we can store the result in a table , we can use memoization.

"""

def cuttingRod_memo(price, N):
    memo = [0 for x in range(N+1)]
    for i in range(1, N+1):
        for j in range(i):
            memo[i] = max(memo[i], price[j] + memo[i-j-1])
    return memo[N]


if __name__ == '__main__':
    array = [1 ,2, 3, 4]
    price = [1 ,5, 8, 9]
    N = len(array)
    print(cuttingRod(price, N))
    print(cuttingRod_memo(price, N))

    array = [1, 2, 3, 4, 5, 6, 7, 8 ]
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    N = len(array)
    print(cuttingRod(price, N))
    print(cuttingRod_memo(price, N))