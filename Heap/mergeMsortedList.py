"""
Merge M sorted List:

Input: 4 sorted lists of variable length
 
[ 10, 20, 30, 40 ]
[ 15, 25, 35 ]
[ 27, 29, 37, 48, 93 ]
[ 32, 33 ]

O/P : 10 15 20 25 27 29 30 32 33 35 37 40 48 93


Approach: Construct a min heap of size M and insert the first element of ach 
list into it.
Then pop the root (which is min) from the heap and insert the next element
from the same list which is poped.
repeat till the heap exhausted.

"""

#refcode: https://www.techiedelight.com/merge-m-sorted-lists-variable-length/
import heapq
from heapq import heappop, heappush
import time

class Node: 

    def __init__(self, value, list_num, index):

        self.value = value # element @consideration
        self.list_num = list_num # list number of element
        self.index = index # column number of the list from which element was taken

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f'Node value: {self.value}, From which List: {self.list_num}'

def sortedArray(list):
    result = []
    # Insert the first element from each array 
    pq = [Node(list[i][0], i, 0) for i in range(len(list)) if len(list[i])>=1]
    heapq.heapify(pq)
    print(pq)
    while pq:
        # extract the element
        min_ele = heappop(pq)
        result.append(min_ele.value)
        # take next element from same list and insert it to min-heap
        if min_ele.index + 1 < len(list[min_ele.list_num]):
            min_ele.index += 1
            min_ele.value = list[min_ele.list_num][min_ele.index]
            heappush(pq, min_ele)
    return result

if __name__ == '__main__':
    
  list = [[ 10, 20, 30, 40 ],
          [ 15, 25, 35 ],
          [ 27, 29, 37, 48, 93 ],
          [ 32, 33 ]
  ]
  print(sortedArray(list))

  list = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
  print(sortedArray(list))