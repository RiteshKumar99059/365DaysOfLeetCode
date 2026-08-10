class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        for i in s:
            stack.append(i)
        
        for i in range(len(s)):
            s[i] = stack.pop()

        return s



        