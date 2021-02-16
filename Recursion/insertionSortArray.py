"""
Sort an array recusively.

"""

def insertionSortRecusively(arr, n):
    '''
    arr: an unsorted array.
    n: length of array.

    '''

    # base condition

    if n == 1:
        return
    
    insertionSortRecusively(arr, n-1)
    last = arr[n-1]
    j = n-2

    # move the element of arra that are greater than key
    # to one position ahead of there current position.

    while (j >= 1 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last

if __name__ == '__main__':
    
    arr =  [-5, 14, 15, -1, 3, 0]
    n = len(arr)
    insertionSortRecusively(arr, n)
    print(arr)
