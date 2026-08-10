class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0

        for i in sentences:
            current_count = len(i.split())

            max_count = max(max_count,current_count)
        return max_count
        