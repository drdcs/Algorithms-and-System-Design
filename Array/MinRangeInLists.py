"""
Find smallest range containing elements from k lists

Input: K = 3

arr1[] : [4, 7, 9, 12, 15]
arr2[] : [0, 8, 10, 14, 20]
arr3[] : [6, 12, 16, 30, 50]

Output:
The smallest range is [6 8]

class : Value, ListNum, Column.
Build a heap from the class Nodes.
keep the high value from iteration..
pop the minimum value from the heap
check if high - low < already existing, f so then replace
run until one of the list got exhausted.

"""
import sys
from heapq import heappush, heappop

class Node: 
	def __init__(self, value, list_num, index):
		self.value = value
		self.list_num = list_num
		self.index = index	
	def __lt__(self, other):
        return self.value < other.value
    
        
def findMinRange(list):
	high = -sys.maxsize
	pointer = (0, sys.maxsize)
	heap = []
	for i in range(len(list)):
		heappush(heap, Node(list[i][0], i, 0))
		high = max(high, list[i][0])
	
	while True:
		top = heappop(heap)
		low = top.value
		listnumber = top.list_num
		columnIndex = top.index
		
		if high - low < pointer[1] - pointer[0]:
			pointer = (low, high)
			
		if columnIndex == len(list[listnumber]) -1:
			return pointer
			
		# if not take the element from the same list and
		# insert it into the min heap
		heappush(heap, Node(list[listnumber][columnIndex+1], listnumber, columnIndex))
		high = max(high, list[listnumber][columnIndex+1])
		
			
		
		
	
if __name__ == '__main__':
	lists = [[4, 7, 9, 12, 15],[0, 8, 10, 14, 20],[6, 12, 16, 30, 50]]
	print(findMinRange(lists))
	