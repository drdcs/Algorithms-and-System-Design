"""
Given that integers are being read from a data stream. 
Find the median of all the elements read so far starting from 
the first integer till the last integer. 
This is also called the Median of Running Integers. 
The data stream can be any source of data, for example, a file,
an array of integers, input stream etc.

nput: 5 10 15
Output: 5, 7.5, 10
Explanation: Given the input stream as an array of integers [5,10,15]. 
Read integers one by one and print the median correspondingly. 
So, after reading first element 5,median is 5. 
After reading 10,median is 7.5 After reading 15 ,median is 10.

"""

# process

# step 1: Add the value to the max heap.
# step 2: remove the top of the max heap and add it to the min heap.
# step 3: if the max heap size is less than the min heap then remove the top of min heap
#         add it to the max heap.
# step 4: Finding the median: If the size of max heap is greater than min heap
#         then peak the op of the max heap as Median.
#         If both the max heap and min heap of same size then peak the top of
#         max heap and top of min heap , divide it by 2 to get the median.


#### code: 


from heapq import heappop, heappush, heappushpop

class MedianFinder:

    def __init__(self):
        
        """
        Initialize the data structure
        """
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')] 

        # in python heap is bu default the min-heap , so we need to define a max heap
        # trick is to enter the element -ve

    def addNum(self, num):

        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]

        if num > upperMin or (lowerMax <= num <= upperMin and len(self.upperHeap) == len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)

        if len(self.upperHeap) - len(self.lowerHeap) > 1:
            heappush(self.lowerHeap, -heappop(self.upperHeap))
            
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush(self.upperHeap, -heappop(self.lowerHeap))
    
    def findMedian(self):

        if len(self.upperHeap) == len(self.lowerHeap):
            upperMin = + self.upperHeap[0]
            lowerMax = - self.lowerHeap[0]
            return (float(upperMin) + float(lowerMax))/ 2.0
        else:
            assert len(self.upperHeap) == len(self.lowerHeap) + 1
            return float(self.upperHeap[0])

if __name__ == '__main__':

    mf = MedianFinder()
    mf.addNum(2)
    mf.addNum(1)
    print(mf.findMedian())
    
    mf.addNum(3)
    mf.addNum(10)
    print(mf.findMedian())

    mf.addNum(7)
    mf.addNum(10)
    print(mf.findMedian())

    mf.addNum(-1)
    mf.addNum(-2)
    print(mf.findMedian())
