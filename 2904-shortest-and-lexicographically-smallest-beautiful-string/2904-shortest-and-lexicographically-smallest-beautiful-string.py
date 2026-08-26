class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        answer = ''
        left = 0
        count = 0

        for i in range(n):
            if s[i] == '1':
                count += 1

            while count == k:
                while s[left] == "0":
                    left +=1

                current = s[left : i + 1]

                if not answer or len(current) < len(answer) or (len(current) == len(answer) and current < answer):
                    answer = current

                if s[left] == '1':
                    count -= 1
                left += 1

        return answer
        