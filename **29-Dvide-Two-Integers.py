class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 1
        sign = 1
        if dividend < 0:
            sign = self.opposite(sign)
            dividend = self.opposite(dividend)
            
        if divisor < 0:
            sign = self.opposite(sign)
            divisor = self.opposite(divisor)
            
        if dividend < divisor:
            return 0
        
        origin_dividend = dividend
        origin_divisor = divisor
        
        dividend -= divisor
        #every time divisor = 2*divisor, which helps to avoid time out. 
        while divisor <= dividend:
            ans = ans + ans
            divisor += divisor
            dividend -= divisor

        a = ans + self.divide(origin_dividend - divisor, origin_divisor)
        a = int(a) if sign > 0 else self.opposite(a)
        #avoid overflow
        if -2**31 <= a <= 2**31-1:
            return a
        else:
            return 2**31-1
        
     #caculate -x, which is the complement code of x
    def opposite(self, x):
        return ~x+1
       