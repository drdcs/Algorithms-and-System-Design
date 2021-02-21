"""
Given array of integers return pair of numbers of a given sum.

arr = [1, 9, 1, 9], 10 => (1,9), (1,9)
arr = [1, 9, 1], 10 => (1, 9)
arr = [0, 1, 4, 9, 6] => (1,9), (6,4)

"""
def pairSum(arr, target):
    arr.sort() # nlogn
    i = 0
    j = len(arr)-1
    res = []
    while(i < j):
        currSum = arr[i] + arr[j]
        if currSum < target:
            i += 1
        elif currSum > target:
            j -= 1
        else:
            res.append([arr[i], arr[j]])
            i += 1
            j -= 1
    return res


if __name__ == '__main__':
    arr1 = [1, 9, 1, 9]
    arr2 = [1, 9, 1]
    arr3 = [1, 9, 6, 4]
    target = 10
    print(pairSum(arr1, target))
    print(pairSum(arr2, target))
    print(pairSum(arr3, target))