def rec_search(array, left, right, item):
    #base case
    if right < left:
        return -1
    if array[right] == item:
        return item
    if array[left] == item:
        return item
    return rec_search(array, left+1, right-1, item)

arr = [12, 34, 54, 2, 3] 
n = len(arr) 
x = 3
print(rec_search(arr, 0, n-1, x))