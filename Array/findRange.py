"""
Given an array containing only 0s and 1s, find the largest subarray which contains equal no of 0s and 1s. 
The expected time complexity is O(n). 
Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 1 to 6 
(Starting and Ending indexes of output subarray)

"""

def maxLenOfArray(arr, n):
	
	hashmap = {}
	max_len = 0
	curr_sum = 0
	ending_index = -1
	
	# just convert the 0 to -1
	
	for i in range(len(arr)):
		if(arr[i] == 0):
			arr[i] = -1
	
	for i in range(0, n):
	
		curr_sum += arr[i]
		
		if(curr_sum == 0):
			max_len = i + 1
			ending_index = i
			
		if curr_sum in hashmap:
			if max_len < i - hashmap[curr_sum]:
				max_len = i - hashmap[curr_sum]
				ending_index = i
		else:
			hashmap[curr_sum] = i
			
	return f"range : {ending_index-max_len+1}, {ending_index}"
			
if __name__ == '__main__':
	arr = [1, 0, 1, 1, 1, 0, 0]
	print(maxLenOfArray(arr, len(arr)))