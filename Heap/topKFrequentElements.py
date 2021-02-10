"""
Find k numbers with most occurrences in the given array

Given an array of n numbers and a positive integer k. 
The problem is to find k numbers with most occurrences, 
i.e., the top k numbers having the maximum frequency.
If two numbers have the same frequency 
then the larger number should be given preference.

Input: 
arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, 
k = 2
Output: 4 1
Explanation:
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and
4 is larger than 1.

"""
import heapq
from collections import Counter


def topKFrequent(arr, k):
    res = []
    dic = Counter(arr)
    max_heap = [(-val, key) for key, val in dic.items()]
    heapq.heapify(max_heap)
    for _ in range(k):
        res.append(heapq.heappop(max_heap)[1])
    return res 

# Driver code
if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1,6,6]
    n = 8
    k = 2
    print(topKFrequent(arr, k))