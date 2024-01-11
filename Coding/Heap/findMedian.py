#https://leetcode.com/problems/find-median-from-data-stream/

import heapq
class MedianFinder1(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = 0

# 1 0 2 3 4
# [1] []
# [1] [0]
# [1, 0] [2]
# [1, 0] [2, 3]
# [1, 0, 2] [3, 4]


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #even
        print("before" , self.count)
        if self.count % 2 == 0:
            if self.count > 0:
                c,n = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-c, n))
                self.count += 1
                heapq.heappush(self.min_heap, (self.count, num))
            else:
                self.count += 1
                heapq.heappush(self.max_heap, (-self.count, num))
                
        #odd
        else:
            self.count += 1
            heapq.heappush(self.min_heap, (self.count, num))
        print("after" , self.count)

        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count % 2 == 0 :
            left = self.min_heap[0][1] 
            right = self.max_heap[0][1]
            median  = (left + right ) / 2 
            print( left, right, median)
        else:
            median = left = self.max_heap[0][1] 
            print(median)
        return median
        


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0





# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

obj.addNum(6)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(1)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())