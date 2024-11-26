class Solution:
    import sys
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=sys.maxsize
        maxProfit=0
        n=len(prices)

        for i in range(n):
            if prices[i]<minPrice:
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit


        



