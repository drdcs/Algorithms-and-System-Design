"""
Given an Array of numbers, {1,2,1}. find out the count of subset that achieves a given sum.
Array = [1, 2, 1]
Sum = 3
ans: 2


      0  |  1  | 2  | 3
    -----------------------
0  |  1  |  0  | 0  | 0  
    -----------------------
1  |  1  |  1  | 0  | 0 
    -----------------------
2  |  1  |  1  | 1  | 1
    -----------------------
1  |  1  |  2  | 2  | 2 
    -----------------------
"""

def countSubset(array, W, N):
    Matrix = [[0 for i in range(W+1)] for j in range(N+1)]
    
    for i in range(N+1):
        Matrix[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, W+1):
            if array[i-1] > j:
                Matrix[i][j] = Matrix[i-1][j]
            else:
                Matrix[i][j] = (Matrix[i-1][j] + Matrix[i-1][j- array[i-1]])
    return Matrix[-1][-1]

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    W = 7
    N = len(array)
    print(countSubset(array, W, N))
    print("/n######")
    array = [2, 3, 5, 6, 8, 10]
    W = 10
    N = len(array)
    print(countSubset(array, W, N))
    print("/n######")
    array = [1, 2, 1]
    W = 3
    N = len(array)
    print(countSubset(array, W, N))