"""
You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost 
or the rightmost element from the array nums and subtract 
its value from x. Note that this modifies the array 
for future operations.

Return the minimum number of operations to reduce x to exactly 0 
if it's possible, otherwise, return -1.

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements 
to reduce x to zero.
{1,1,3} and {2,3} => {2,3} is min .. 2

"""

def minOperations(array, X, L, R, Count, mem):

    # base condition
    if X == 0:
        return Count
    elif (X < 0 or L > R):
        return 1e6

    else:
        key = str(L) + "*"+ str(R) + "*" + str(X)

        # Logic
        Left = minOperations(array, X-array[L], L+1, R, Count+1, mem)
        Right = minOperations(array, X-array[R], L, R-1, Count+1, mem)
        mem[key] = min(Left, Right)
    return min(Left, Right)

if __name__ == '__main__':

    nums = [1,1,4,2,3]
    X = 5
    L = 0
    R = len(nums)-1
    Count = 0
    mem = {}
    print(minOperations(nums, X, L, R, Count, mem))

    nums = [1,1,14,2,13]
    X = 5
    L = 0
    R = len(nums)-1
    Count = 0
    mem = {}
    res = minOperations(nums, X, L, R, Count, mem)
    res = -1 if res == 1e6 else res
    print(res)

