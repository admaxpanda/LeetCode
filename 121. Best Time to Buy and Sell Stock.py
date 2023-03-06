class Solution:
    def maxProfit(self, prices):
        ans=0
        for i in range(len(prices)-1):
            for k in range(i+1,len(prices)):
                ans=max(ans,prices[k]-prices[i])
        return ans
s=Solution()
print(s.maxProfit(prices=[7,1,5,3,6,4]))