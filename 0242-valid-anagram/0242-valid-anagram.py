class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in t:
        #     if i in s:
        #         return True
        #     else:
        #         return False
        #         s.remove(i)

        # a = sorted(s)
        # b = sorted(t)

        # return a == b

        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            
            count[ch] -= 1
            
            if count[ch] < 0:
                return False

        return True



