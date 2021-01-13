# https://www.youtube.com/watch?v=4CykZVqBuCw&list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv&index=2

# worst / Average : O(N^2) 

def selection_sort(sequence):

    length = len(sequence)

    for i in range(0, length-1):
        min_value = i

        for j in range(i+1, length):
            if array[j] < sequence[min_value]:
                min_value = j
        if min_value != sequence[i]:
            sequence[min_value], sequence[i] = sequence[i] ,sequence[min_value]

    return sequence

array = [1, 2, 6, 7, 8 , 5 , 6 , 9]
print(selection_sort(array))