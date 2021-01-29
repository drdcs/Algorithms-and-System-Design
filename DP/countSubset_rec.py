"""
Given an Array of numbers, {1,2,1}. find out the count of subset that achieves a given sum.
Array = [1, 2, 1]
Sum = 3
ans: 2

Approach 1: Recursion. We build a recursion tree:
 we have 2 choices either include it or exclude it.
                     
                     1
                 /       \ 
                2         2
              /  \      /   \ 
            1    1     1    1 
          /  \  /  \  / \  / \ 
"""

def countSubset(array, W, N):
    # base condition
    if W == 0:
        return 1
    if N == 0:
        return 0

    # excude if given number is greater than the W
    if (array[N-1] > W):
        return countSubset(array, W, N-1)
    # else 2 choices , either include or exclude..
    else:
        return countSubset(array, W, N-1) + countSubset(array, W - array[N-1], N-1)

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    W = 7
    N = len(array)
    print(countSubset(array, W, N))