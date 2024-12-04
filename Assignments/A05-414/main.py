import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        counter = 0
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
                counter = counter + 1
        unique = sorted(set(nums), reverse=True)
        print(unique)

        if counter < 3:
            num = heapq.nlargest(1, unique)[0]
            return int(num)
        else:
            return unique[2]
