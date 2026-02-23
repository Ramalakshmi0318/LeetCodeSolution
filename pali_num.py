class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Special cases:
        # 1. Negative numbers are not palindromes (e.g., -121 != 121-)
        # 2. If the last digit is 0, the first must be 0 (only 0 itself fits)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            # Move the last digit of x to reverted_number
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is odd, we can get rid of the middle digit by reverted_number // 10
        # For example, if x = 121, at the end of loop x = 1, reverted_number = 12
        return x == reverted_number or x == reverted_number // 10
