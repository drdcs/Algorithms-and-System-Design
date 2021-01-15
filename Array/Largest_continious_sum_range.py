Array = [-2, -3, 4, -1, -2, 1, 5, -3]

def largest_continious_sum_idx(array):

    max_so_far = max_here = float("-inf")
    startIdx = endIdx = 0
    pointer = 0

    for index in range(0, len(array)):
        max_here = array[index]
        if max_here > max_so_far:
            max_so_far = max_here
            startIdx = pointer
            endIdx = index
        if max_here < 0:
            max_here = 0
            pointer += 1
    return (startIdx, endIdx)

print(largest_continious_sum_idx(Array))
