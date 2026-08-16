class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        n = len(s)
        # if n < 3:
        #     return s

        for i in range(n):
            for j in range(i,n):
                sl = s[i:j+1]
                if sl == sl[::-1]:
                    if len(sl) > len(res):
                        res = sl
        return res
            
        
        