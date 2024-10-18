import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

      largest = heapq.nlargest(k, nums)


      return largest[k-1]
