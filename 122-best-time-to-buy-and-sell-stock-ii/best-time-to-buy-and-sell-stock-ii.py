class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = sys.maxsize
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            maxProfit += prices[i] - minPrice
            minPrice=prices[i]

        return maxProfit