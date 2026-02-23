class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        # Use the first string as the reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Compare this character with the same index in all other strings
            for j in range(1, len(strs)):
                # If index is out of bounds or characters don't match, return result
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]
