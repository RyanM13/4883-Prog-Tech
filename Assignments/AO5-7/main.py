class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            if -int(x) < -2**31-1:
                return 0
            else:
                return -int(x)
        else:
            x = str(x)
            x = x[::-1]
            if int(x) > 2**31-1:
                return 0
            else:
                return int(x)
