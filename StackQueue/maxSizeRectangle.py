"""
Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

Example: 

Input:
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
Output :
1 1 1 1
1 1 1 1

Explanation : 
The largest rectangle with only 1's is from 
(1, 0) to (2, 3) which is
1 1 1 1
1 1 1 1 

Illustartion:

Input :
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
Step 1: 
0 1 1 0  maximum area  = 2
Step 2:
row 1  1 2 2 1  area = 4, maximum area becomes 4
row 2  2 3 3 2  area = 8, maximum area becomes 8
row 3  3 4 0 0  area = 6, maximum area remains 8


"""

def max_area_histogram(histogram):
    l_stack = list()
    r_stack = list()
    left = [-1] * len(histogram)
    right= [-1] * len(histogram)

    n = len(histogram)

    # fill left

    for i in range(0,n):

        if (not l_stack):
            left[i] = 0
            l_stack.append(i)
        
        else:
            
            while (l_stack) and (histogram[l_stack[-1]] >= histogram[i]):
                l_stack.pop()
            left[i] = 0 if not l_stack else l_stack[-1]+1 # add +1
            l_stack.append(i)
    
    # fill right
    for i in reversed(range(n)):
        if(not r_stack):
            right[i] = n - 1
            r_stack.append(i)
        else:
            while(r_stack and (histogram[r_stack[-1]] >= histogram[i])):
                r_stack.pop()
            right[i] = n-1 if not r_stack else r_stack[-1]-1
            r_stack.append(i)

    # get the area
    area = 0
    for i in range(n):
        curr = ((right[i] - left[i])+ 1)* histogram[i]
        area = max(area, curr)
    return area


def maxRectangle(A):
    result = max_area_histogram(A[0])
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if A[i][j]:
                A[i][j] += A[i-1][j]
        t_result = max_area_histogram(A[i])
        result = max(result,t_result)
    return result

if __name__ == '__main__':

    A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    print(maxRectangle(A))