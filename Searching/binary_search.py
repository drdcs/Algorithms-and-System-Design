def binary_search(sequence, item):

    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        middle_point = begin_index + (end_index - begin_index) // 2
        middle_value = sequence[middle_point]
        if middle_value == item:
            return middle_value
        elif item < middle_value:
            end_index = middle_point - 1
        else:
            begin_index = middle_point + 1
    return None

array = [8, 2, 6, 7, 1 , 5 , 6 , 1]
print(binary_search(array, 11))