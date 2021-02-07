"""
Input: k = 3
 
List 1: 1 -> 5 -> 7 -> NULL
List 2: 2 -> 3 -> 6 -> 9 -> NULL
List 3: 4 -> 8 -> 10 -> NULL
 
Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> NULL

"""
import heapq
from heapq import heappush, heappop
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # def __repr__(self):
    #     return f"Node: {self.data}"

    def __lt__(self, other):
        return self.data < other.data

def printList(node):
    while node:
        print(node.data, end='->')
        node = node.next
    print("None")

# main function is to merge k sorted linked list..
# it takes a list of size k

def mergeKs(list):
    # create a min-heap using first node of each list
    pq = [x for x in list]
    heapq.heapify(list)
    # take two pointers head and tails where
    # head points to the first node of the o/p
    # list and tail point to its last node

    head = last = None

    while pq:
        # extract minimum node from the min-heap
        min_ele = heappop(pq)
        # add the minimum node to o/p list
        if head is None:
            head = min_ele
            last = min_ele
        else:
            last.next = min_ele
            last = min_ele
        # take next node from "same list"
        # insert it into the min-heap
        print(min_ele.data)
        if min_ele.next:
            heappush(pq, min_ele.next)
    return head

if __name__ == '__main__':
    k = 3
    lists = [None] * k
    lists[0] = Node(1)
    lists[0].next = Node(3)
    lists[0].next.next = Node(7)

    lists[1] = Node(2)
    lists[1].next = Node(3)
    lists[1].next.next = Node(6)
    lists[1].next.next.next = Node(9)

    lists[2] = Node(4)
    lists[2].next = Node(8)
    lists[2].next.next = Node(10)

    head = mergeKs(lists)
    printList(head)

