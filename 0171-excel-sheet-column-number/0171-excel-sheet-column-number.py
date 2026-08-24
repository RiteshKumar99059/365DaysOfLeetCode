class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        answer = 0

        for i in columnTitle:
            value = ord(i) - ord('A') + 1
            answer = answer * 26 + value

        return answer
        