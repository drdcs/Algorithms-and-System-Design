"""
Largest Rectangular Area in a Histogram

Find the largest rectangular area possible in a given histogram 
where the largest rectangle can be made of a number of contiguous bars. 
For simplicity, assume that all bars have same width 
and the width is 1 unit.

For example, 

consider the following histogram with 7 bars of 
heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible 
is 12.


|---|
|   |    ---
|   |   |   |---
|   |   |   |   |
|   |---|   |   |
|   |   |   |   |---|
------------------------------


Idea: Traverse the array from left to right and store the max value  keep the 

Dry Run:                  Time   Space
       0  1  2  3  4  5
Bar  : 2  1  5  6  2  3 
left : 0  0  2  3  2  5   O(N)    O(N)
right: 0  5  3  3  5  5   O(N)    O(N)
---------------------------------------------
Area : 2  6  10 6  8  3   O(1)    O(1)/0(N)
---------------------------------------------
                          O(N)    O(N)

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


if __name__ == '__main__':
    histogram = [2 ,1 ,5  ,6  ,2  ,3]
    print(max_area_histogram(histogram))


