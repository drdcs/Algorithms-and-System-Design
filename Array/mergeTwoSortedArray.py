def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1+n2)
    i = 0 # arr1 pointer
    j = 0 # arr2 pointer
    k = 0 # pointer to keep track of third pointer
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1

    # store the remaining elements of first array.

    while i < n1:
        arr3[k] = arr1[i]
        k += 1
        i += 1
    
    while j < n2:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    return arr3

if __name__ == '__main__':
    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]
    n1 = len(arr1)
    n2 = len(arr2)
    print(mergeArrays(arr1, arr2,n1, n2 ))