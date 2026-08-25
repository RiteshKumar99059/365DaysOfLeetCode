class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        missing = k

        for i in nums:
            if i == missing:
                missing += k

        return missing


        