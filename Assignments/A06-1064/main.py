import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones) > 1):
            largest = heapq.nlargest(2, stones)
           
            stones.remove(largest[0])
            stones.remove(largest[1])

            if(largest[0] != largest[1]):
                stones.append(largest[0] - largest[1])
        
        return stones[0] if stones else 0

            
        
