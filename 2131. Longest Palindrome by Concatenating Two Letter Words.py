class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for i in d:
            if(i in d and i[::-1] in d):
                if(i==i[::-1]):
                    ans+=d[i]//2*4
                    d[i]-=d[i]//2*2
                else:
                    minn=min(d[i],d[i[::-1]])
                    ans+=4*minn
                    d[i]-=minn
                    d[i[::-1]]-=minn
        
        for i in d:
            if(d[i]>0 and i[0]==i[1]):
                ans+=2
                break
        return ans
s=Solution()
print(s.longestPalindrome(["lc","cl","gg"]))