"""
Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000  
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30


Input: p[] = {10, 20, 30, 40, 30} 
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

"""

def matrixMultiplication(p, i, j, T):
    if i == j:
        return 0
    _cost = float('inf')

    if T[i][j] == -1:
        for k in range(i,j):
            temp = (matrixMultiplication(p, i, k,T) + \
                matrixMultiplication(p, k+1, j,T) + \
                    p[i-1] * p[k] * p[j])
            if temp < _cost:
                _cost = temp
        T[i][j] = _cost

    return _cost

if __name__ == '__main__':
    arr =  [1,2,3,4]
    n = len(arr)
    T = [[-1 for x in range(len(arr))] for j in range(len(arr))]   
    print(matrixMultiplication(arr,1,n-1,T))