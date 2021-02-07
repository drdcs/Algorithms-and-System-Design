"""
Given two arrays such that the two arrays have some common elements.
Find sum of the maximum sum path to reach from beginning of  
any two array to end of two arrays.

we can switch from one array to another array only at common elements.

Note: common elements don't have the same indices.

How to approach ?

arr1 = [2,3,7,10,12]
arr2 = [1,5,7,8]
o/p = 35 => 1 + 5 + 7 + 10 +12

add the sum of two arrays till the intersection point.compare the two sums and
add the result of the larger sum to the array.


"""

def maxPathSum(arr1, arr2, m, n):
    idx1, idx2 = 0, 0
    result, sum1, sum2 = 0 , 0 , 0
    while(idx1 < m and idx2 < n):
        # do a compare and add sum value
        if arr1[idx1] < arr2[idx2]:
            sum1 += arr1[idx1]
            idx1 += 1

        elif arr1[idx1] > arr2[idx2]:
            sum2 += arr2[idx2]
            idx2 += 1

        else:
            result += max(sum1, sum2)
            # update the sum back to 0
            sum1, sum2 = 0 ,0 
            
            temp = idx1
            while idx1 < m and arr1[idx1] == arr2[idx2]:
                sum1 += arr1[idx1]
                idx1 += 1

            while idx2 < n and arr1[temp] == arr2[idx2]:
                sum2 += arr2[idx2]
                idx2 += 1

            result += max(sum1, sum2)
            sum1  = sum2 = 0

    while idx1 < m:
        sum1 += arr1[idx1]
        idx1 += 1

    while idx2 < n:
        sum2 += arr2[idx2]
        idx2 += 1
    
    result += max(sum1, sum2)
    return result

if __name__ == '__main__':
    arr1 = [2,3,7,10,12,15,30,34]
    arr2 = [1,5,7,8,10,15,16,19]
    m = len(arr1)
    n = len(arr2)
    print(maxPathSum(arr1, arr2, m, n))
         
