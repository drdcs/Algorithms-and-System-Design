def heapify(array, n, i):
 '''
 array : given array.
 n : length of array.
 i : position at which we need to heapify
 '''
 
 largestEle = i # at position i.
 left = 2*i + 1
 right = 2*i + 2
 
 if left < n and array[left] > array[largestEle]:
   largestEle = left
 
 if right < n and array[right] > array[largestEle]:
   largestEle = right
 
 if largestEle != i:
   array[i], array[largestEle] = array[largestEle], array[i]
   heapify(array, n, largestEle)
 
def buildHeap(array, n):
 parentIdx = n//2 -1
 for i in range(parentIdx, -1, -1):
   heapify(array, n, i)
 
def heapSort(array, n):
 for i in range(n-1,0,-1):
   array[i], array[0] = array[0], array[i]
   heapify(array, i, 0)
 return array
 
if __name__ == '__main__':
 array = [1,3,5,4,6,13,10,9,8,15,17,19]
 n = len(array)
 buildHeap(array, n)
 print("heapify: " ,array)
 heapSort(array, n)
 print("sortedarray",array)
 


"""

Heap sort algorithm Sorting Algorithm:

Build Heap + HeapiFy + ExtractMax/ExtractMin
 O(N)         LOG(N)          (N-1)

total time complexity = NlogN

"""