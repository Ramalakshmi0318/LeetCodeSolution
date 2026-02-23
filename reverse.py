class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit boundaries
        MIN, MAX = -2**31, 2**31 - 1
        
        # Handle the sign and absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x != 0:
            # Extract last digit
            pop = x % 10
            x //= 10
            
            # Reconstruct the number
            res = (res * 10) + pop
            
        # Reapply sign
        res *= sign
        
        # Final overflow check
        if res < MIN or res > MAX:
            return 0
            
        return res
