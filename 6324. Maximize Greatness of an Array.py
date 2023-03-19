class Solution:
    def maximizeGreatness(self, nums: int) -> int:
        d={}
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        ans=0
        lower=0
        for i in d:
            ans+=min(d[i],lower)
            lower=max(lower-d[i],0)
            lower+=d[i]
        return ans
s=Solution()
print(s.maximizeGreatness([1,2,3,4]))
