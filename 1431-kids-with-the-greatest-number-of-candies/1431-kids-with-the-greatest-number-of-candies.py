class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum = max(candies)
        n=len(candies)

        for i in range(0,n):
            if candies[i] + extraCandies < maximum:
                result.append(False)
            else:
                result.append(True)
        return result

        