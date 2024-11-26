class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        minPrice=sys.maxsize
        totalProfit=0

        for i in range(n):
            currPrice = prices[i]
            if currPrice < minPrice:
                minPrice = currPrice
            else:
                totalProfit += currPrice-minPrice
                minPrice = currPrice

        return totalProfit


        