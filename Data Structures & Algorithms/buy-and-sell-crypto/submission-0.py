class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=1
        l=0
        profit=0

        while r<len(prices):
            if prices[r]>prices[l]:
                p=prices[r]-prices[l]
                profit= max(profit, p)
            else:
                l=r
            r+=1
        return profit

