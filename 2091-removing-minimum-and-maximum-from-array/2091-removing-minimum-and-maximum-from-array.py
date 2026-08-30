class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        i = min(min_index,max_index)
        j = max(min_index,max_index)

        return min(j + 1, n - i, (i + 1) + (n - j))