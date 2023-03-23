class Solution:
    def longestCommonPrefix(self, strs):
        short = min(strs, key=len) 
        for word in strs: 
            while len(short) > 0:
                if word.startswith(short): 
                    break
                else:
                    short = short[:-1] 
        return short
