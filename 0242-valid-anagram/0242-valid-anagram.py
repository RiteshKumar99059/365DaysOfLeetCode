class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in t:
        #     if i in s:
        #         return True
        #     else:
        #         return False
        #         s.remove(i)
        a = sorted(s)
        b = sorted(t)

        return a == b