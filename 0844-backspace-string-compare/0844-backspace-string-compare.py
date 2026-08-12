class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string : str):
            stack =[]

            for i in string:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s) == build(t)

         
        