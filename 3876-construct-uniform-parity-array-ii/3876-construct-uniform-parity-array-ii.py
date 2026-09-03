class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_value = min(nums1)

        odd = any(x % 2 != 0 for x in nums1)
        if not odd:
            return True
        return min_value % 2 != 0
        