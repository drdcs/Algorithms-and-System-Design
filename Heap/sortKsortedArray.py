"""
Given a K-sorted array that is almost sorted such that
each element may be misplaced by k positions from the correct
order.

Idea:

we can solve O(nlogk) using min heap.
Step 1:

idea is to build a min-heap of size k+1
and insert fist k+1 element into that.

Step 2: Then we extract the min from the heap and
insert the next element from the heap.

Step 3: Continue the above process until the we exhaust of the heap.


"""
import heapq
from heapq import heappush, heappop

def sort_k_sorted_arr(array, k):
    
    # create a min-heap from first k+1 elemeent.
    heap_construction = array[0:k+1]
    heapq.heapify(heap_construction)

    # do remaining element from list
    index = 0
    for idx in range(k+1, len(array)):
        # pop the element from list
        # add next element.
        array[index] = heappop(heap_construction)
        index += 1
        heappush(heap_construction, array[idx])

    while heap_construction:
        array[index] = heappop(heap_construction)
        index += 1

if __name__ == '__main__':
    list = [1,4,5,2,3,7,8,6,10,9]
    k = 2
    sort_k_sorted_arr(list,k)
    print(list)