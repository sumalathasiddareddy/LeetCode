class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ''' My solution
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
        '''

        #Most voted solution
        profit=0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


        