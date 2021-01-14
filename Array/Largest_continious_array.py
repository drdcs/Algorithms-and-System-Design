'''
Write an efficient program to find the sum of contiguous
subarray within a one-dimensional array of numbers 
which has the largest sum.

[-2, -3, 4, -1, -2, 1, 5, 3]
4 + -1 + -2 + 1 + 5 = 7

'''

def find_largest_conti_array_sum(array):
    current_sum = max_so_far = array[0]

    for index in range(1, len(array)):
        current_sum += array[index]
        if current_sum > max_so_far:
            max_so_far = current_sum
        
        if current_sum < 0:
            current_sum = 0
    return max_so_far


array_1 = [-2, -3, 4, -1, -2, 1, 5, 3]
array_2 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print(find_largest_conti_array_sum(array_1))
print(find_largest_conti_array_sum(array_2))