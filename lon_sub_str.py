class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {} # stores { character: last_seen_index }
        l = 0
        res = 0
        
        for r in range(len(s)):
            # If the character is in the map and within the current window
            if s[r] in charMap and charMap[s[r]] >= l:
                # Move the left pointer past the previous occurrence
                l = charMap[s[r]] + 1
            
            # Update/Insert the last seen index of the character
            charMap[s[r]] = r
            
            # Update the maximum length found
            res = max(res, r - l + 1)
            
        return res
