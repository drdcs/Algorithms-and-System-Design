def quick_sort(sequence):

    """
    :param: unsorted array.
            return sorted array.
    
    consideration : Last element as pivot.

    Average: O(nlogn) | Worst: O(n^2)
    Space: O(N)
    """

    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        # remove last element and return it.
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item) 
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

array = [10, 9, 11, 3, 2, 1, 3, 5]
print(quick_sort(array))

    