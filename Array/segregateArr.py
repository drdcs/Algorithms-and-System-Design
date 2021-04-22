"""

Split array such that -ve numbers at begining 
and +ve numbers at end

input = [-1, 3, 8, -4, 5,-6, 7,-20, 30, 40]
output = [-1, -4, -6, -20, 3,8,30, 40]

"""
def swap(arr, i , j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def segregationOfArrays(arr):

	i = 0
	j = len(arr)-1
	
	while True:
		while (arr[i] < 0 and i < j):
			i += 1
		while (arr[j] > 0 and i<j):
			j -= 1
		if (i < j):
			swap(arr, i, j)
		else:
			break
arr = [-1, 3, 8, -4, 5,-6, 7,-20, 30, 40]		
segregationOfArrays(arr)
print(arr)
			
		
		
		


