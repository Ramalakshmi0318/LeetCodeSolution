class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of Roman numeral symbols and their values in descending order
        roman_map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]
        
        res = []
        for symbol, value in roman_map:
            if num == 0: break
            
            # Determine how many times this symbol fits into num
            count = num // value
            if count > 0:
                res.append(symbol * count)
                num %= value
                
        return "".join(res)
