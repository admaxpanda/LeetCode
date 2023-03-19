class Solution:
    def findScore(self, nums) -> int:
        dic={}
        mark=[False]*len(nums)
        ans=0
        for i in range(len(nums)):
            if(nums[i] in dic):
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        d={}
        for i in sorted(dic):
            d[i]=dic[i]
        for i in d:
            for k in d[i]:
                if not mark[k]:
                    ans+=nums[k]
                    mark[k]=True
                    if(k>0):
                        mark[k-1]=True
                    if(k<len(nums)-1):
                        mark[k+1]=True
        return ans
s=Solution()
print(s.findScore([2,1,3,4,5,2]))
