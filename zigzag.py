class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If there's only one row or string is too short, return as is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to store characters for each row
        rows = [""] * numRows
        currRow = 0
        goingDown = False
        
        for char in s:
            rows[currRow] += char
            
            # If we reach the top or bottom row, change direction
            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown
            
            # Move up or down
            currRow += 1 if goingDown else -1
            
        return "".join(rows)
