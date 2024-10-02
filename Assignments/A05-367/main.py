class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while(num != 0):
            if(num < 0):
                return False
            else:
                num -= i
                i += 2
        return True
         
