class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.copy()

        for i in nums:
            result.append(i)

        return result
        