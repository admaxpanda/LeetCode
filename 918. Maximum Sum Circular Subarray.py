class Solution:
    def maxSubarraySumCircular(self, nums):
        d=nums
        d+=nums
        ans=max(nums)
        for i in range(len(nums)//2):
            if(d[i]<=0):
                continue
            tmp=d[i]
            if(tmp>ans):
                ans=tmp
            for k in range(1,len(nums)//2):
                tmp+=d[i+k]
                if(tmp>ans):
                    ans=tmp
        return ans
s=Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))