# time complexity O(M*N)
# space complexity O(1)

def spiral_copy(inputMatrix, top, bottom, left, right):
    if left > right:
        return
  
  # print top row
    for i in range(left, right+1):
        print(inputMatrix[top][i], end=" ")
    
    top += 1
    
    if top > bottom:
        return
 # print right column
  
    for i in range(top, bottom+1):
        print(inputMatrix[i][right], end= " ")

    right -= 1

    if left > right:
        return
    for i in range(right, left-1, -1):
        print(inputMatrix[bottom][i], end=" ")

    bottom -= 1

    if top > bottom:
        return
    for i in range(bottom, top-1, -1):
        print(inputMatrix[i][left], end = " ")

    left += 1

    spiral_copy(inputMatrix, top, bottom, left, right)
        
if __name__ == '__main__':
    mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]

    top = 0
    bottom = len(mat) -1
    left = 0
    right = len(mat[0]) -1

    spiral_copy(mat, top, bottom, left, right)
