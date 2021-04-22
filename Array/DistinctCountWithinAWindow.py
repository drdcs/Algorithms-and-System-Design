'''
Count distinct elements in every window of size k

Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k.

Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
       k = 4
Output: 3 4 4 3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

'''
from collections import defaultdict
def findDistinctElement(arr, k, n):
	hashset = {}
	dist_count = 0
	result = []
	# insert the first k elements
	hashset = defaultdict(lambda : 0)
	for i in range(k):
      
		if hashset[arr[i]] == 0:
			dist_count += 1
		hashset[arr[i]] += 1
		
	# Travserse the rest of the elements 
	result.append(dist_count)
	
	for i in range(k, n):
		# remove the first elements
		# if there was only one occurance
		# then reduce distinct count
		
		if hashset[arr[i - k]] == 1:
			dist_count -= 1
		hashset[arr[i-k]] -= 1
		
		# add new element
		
		if hashset[arr[i]] == 0:
			dist_count += 1
		hashset[arr[i]] += 1
		
		result.append(dist_count)
		
	return result
    
if __name__ == '__main__':
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    n = len(arr)
    print(findDistinctElement(arr, k, n))
    
		
	
			
	