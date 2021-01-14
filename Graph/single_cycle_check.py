'''
Problem:


You are given an integer where each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of two indices forward in the array. The integer -3 represents a jump of three indices backward in the array.
if a jump spills past the array's bound , it wraps over to the other side. For instance a jump of -1 at index 0 brings us to the last index in the array. Similarly a jump of 1 at the end of the index brings us to index 0.
Write a function that takes an array of integers and return a boolean if the array is a single cycle.


'''

def get_next_element(array, index):
    jump = array[index]
    nextIdx = (index + jump) % len(array)
    return nextIdx if nextIdx >= 0 else len(array) + nextIdx

def single_cycle_check(array):
    numElementVisited = 0
    currentIdx = 0
    while numElementVisited < len(array):
        if numElementVisited > 0 and currentIdx ==0:
            return False
        numElementVisited += 1
        currentIdx = get_next_element(array, currentIdx)
    return currentIdx == 0

array = [2,3,1,-4,-4,2]
print(single_cycle_check(array))