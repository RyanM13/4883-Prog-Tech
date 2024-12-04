class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_num = str(n)

        
        product = 1
        sum = 0
        for digit in str_num:
            product = product * int(digit)
            sum = sum + int(digit)
            
        return product - sum
