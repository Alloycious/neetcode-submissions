class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We're looking for maximum difference between a high and low point
        # in the list.
        # Sell day should always be after buy day of course.
        bought_day, sell_day = 0, 1
        max_profit = 0
        while sell_day < len(prices):
            if prices[bought_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[bought_day]
                max_profit = max(max_profit, profit)
            else:
                # Move buy day to sell day since buying price is higher than selling price
                # as that is the next lowest stock price day to buy in.
                bought_day = sell_day

            # Find the better best price to sell
            sell_day += 1

        return max_profit
