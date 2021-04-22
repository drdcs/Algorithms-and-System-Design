"""
Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: arr2[] is a subset of arr1[]

"""

def isSubSet(arr1, arr2):
	hashset = {}
	for num in arr1:
		if num in hashset:
			hashset[num] += 1
		else:
			hashset[num] = 1
			
	for num in arr2:
		if num in hashset:
			continue
		else:
			return False
	return True
	

if __name__ == '__main__':
	arr1 = [ 11, 1, 13, 21, 3, 7 ]
	arr2 = [ 11, 3, 7, 1 ]
	print(isSubSet(arr1, arr2))