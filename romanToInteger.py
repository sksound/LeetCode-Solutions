class Solution(object):
    def romanToInt(self, s):

         """
        :type s: str
        :rtype: int
        """
        
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        s = s.replace("IX","VIV")
        s = s.replace("IV","IIII")
        s = s.replace("XC","LXL")
        s = s.replace("XL","XXXX")
        s = s.replace("CM","DCD")
        s = s.replace("CD","CCCC")
        for char in s:
            total += vals[char]
        return total
    
  
