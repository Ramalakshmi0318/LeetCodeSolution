class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.lstrip() # Step 1: Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # Step 2: Handle sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Convert digits
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle rounding (overflow/underflow)
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            res = res * 10 + digit
            i += 1
            
        return max(INT_MIN, min(res * sign, INT_MAX))
