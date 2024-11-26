class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        minPrice=sys.maxsize
        totalProfit=0
                
        for i in range(n):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                totalProfit += prices[i]-minPrice
                minPrice = prices[i]

        return totalProfit
       


        