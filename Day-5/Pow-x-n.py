# availiable on leetcode.com
'''
find x to the power n 

wait..  -100.00 < x 100.00

and this enourmous    -2**31   <= n <=   2**31 - 1  

BUT,  -10,000  <=  x**n  <=  10,000  ??  :/
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            inverse = True 
        else:
            inverse = False
            
        
        ans = 1
        while n:
            if n & 1:  # n is odd
                ans *= x
                
            x *= x 
            n >>= 1
        
        
        return 1/ans if inverse else ans
    
# mistakes:  1.)  n can be negative  :'v
#            2.)  n can be zero.  :'v
