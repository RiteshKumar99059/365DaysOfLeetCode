class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maximum_wealth = 0
        
        for i in accounts:
            current_wealth = sum(i)

            maximum_wealth = max(maximum_wealth,current_wealth)

        return maximum_wealth

        