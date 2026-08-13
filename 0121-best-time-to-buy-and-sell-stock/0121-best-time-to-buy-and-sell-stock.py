class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0
        # sell = 1
        # max_profit = 0

        # while sell < len(prices):
        #     current_profit = prices[sell] - prices[buy]
        #     if prices[buy] < prices[sell]:
        #         max_profit = max(current_profit,max_profit)
        #     else:
        #         buy = sell
        #     sell+=1
        # return max_profit
        
        min_price = float('inf')
        max_price = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_price:
                max_price = i - min_price
        return max_price