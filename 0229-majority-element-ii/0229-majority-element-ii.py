class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        return [num for num, j in count.items() if j > len(nums) // 3]