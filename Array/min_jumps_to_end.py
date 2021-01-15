'''

Given an array of integers where each element represents the max number of steps that 
can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array 
(starting from the first element). If an element is 0, then we cannot move through that element.'

Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)

'''

def find_min_jump_to_end_dp(array, length):

    if array[0] == 0:
        return -1
    if length <= 1:
        return 1
    
    maxReach = array[0] # dynamic and changable
    step = array[0] # possible steps.
    jumps = 1 # because we anyway takes a step

    for index in range(1, length):

        if (index == length-1):
            return jumps

        maxReach = max(maxReach, array[index] + index)
        step -= 1

        if step == 0:

            # check if we can make a jump or not

            if (index >= maxReach):
                return -1

            # update the step
            step = maxReach - index
            # As no steps left we need to take a jump
            jumps += 1

    return -1



def find_min_jumps_to_end(array, start, end):

    if start == end:
        return 0
    
    if array[start] == 0:
        return float('inf')
    min = float('inf')
    for i in range(start+1, end+1):
        if (i < start + array[start] + 1):
            jumps = find_min_jumps_to_end(array, i, end)
            if jumps != float('inf') and jumps + 1 < min:
                min = jumps + 1
    return min

array = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(find_min_jumps_to_end(array, 0, len(array)-1))
print(find_min_jump_to_end_dp(array, len(array)-1))
print("this", min_jumps_novice(array))

array = [1, 3, 1, 0, 0, 1, 1, 2, 2, 1,1,1,1,1,1,1,1,1]
print(find_min_jumps_to_end(array, 0, len(array)-1))
print(find_min_jump_to_end_dp(array, len(array)-1))