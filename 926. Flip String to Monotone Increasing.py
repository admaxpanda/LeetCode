class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans=float('inf')
        for i in range(len(s)+1):
            tmp=0
            for k in range(i):
                if(s[k]=='1'):
                    tmp+=1
            for k in range(i,len(s)):
                if(s[k]=='0'):
                    tmp+=1
            ans=min(ans,tmp)
        return ans

s=Solution()
print(s.minFlipsMonoIncr(s='00011000'))