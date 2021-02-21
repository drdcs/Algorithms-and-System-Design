"""
Given an array: [1,1,2,3,3,4,4,5,5,5,5,5]
Find most frequent element.

"""


def frequent_element(arr):
    
    if len(arr) <= 1:
        return arr
    
    hashT = {}
    # rest element push to a hash table
    for element in arr:
        if element in hashT:
            hashT[element] += 1
        else:
            hashT[element] = 1
    
    maxNum = 0
    maxElem = float('-inf')
    
    # traverse through the hashtable and get the max element.
    for ele, val in hashT.items():
        if maxNum < val:
            maxNum = val
            maxElem = ele
    return maxElem

# Time complexity is O(N) 
# Space Complexity is O(N) # worst case

import heapq 

def frequent_element_heap(arr):
    
    if len(arr) <= 1:
        return arr
    
    hashT = {}
    # rest element push to a hash table
    for element in arr:
        if element in hashT:
            hashT[element] += 1
        else:
            hashT[element] = 1
    
    # push the element from heap

    heap = [(value, key) for key, value in hashT.items()]
    largest = heapq.nlargest(1, heap)
    return largest
    # log(d) + o(n) => log d to extract top element , O(n) to build the hash Table
    # d = distinct element in the array.
    # o(d) = auxilary space

if __name__ == '__main__':
    arr = [6,6,6,6,6,6,6,1,1,2,3,3,4,4,5,5,5,5,5,5,5,5]
    print("Top frequent element: ", frequent_element(arr))
    print(frequent_element(arr))



