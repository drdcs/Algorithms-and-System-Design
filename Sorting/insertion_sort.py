def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        value_to_sort = sequence[i]
        while sequence[i-1] > value_to_sort and i > 0:
            sequence[i] , sequence[i-1] = sequence[i-1], sequence[i]
            i -= 1
    return sequence

print(insertion_sort([8, 2, 6, 7, 1 , 5 , 6 , 1]))