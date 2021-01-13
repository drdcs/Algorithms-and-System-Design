def bubble_sort(sequence):
    length_list = len(sequence)-1
    sorted = False
    while not sorted:
        sorted = True
        for index in range(0, length_list):
            if sequence[index] > sequence[index+1]:
                sorted = False
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index]
    return sequence

array = [8, 2, 6, 7, 1 , 5 , 6 , 1]
print(bubble_sort(array))