from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:


        freq =  {}
        left = 0
        ans = 0


        for i in range(len(s)):

            freq[s[i]] = freq.get(s[i],0) + 1


            while freq[s[i]] > 2:

                freq[s[left]] -= 1
                left += 1
            ans = max(ans,i - left + 1)
        return ans

