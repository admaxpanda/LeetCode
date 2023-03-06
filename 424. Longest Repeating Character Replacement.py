class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        maxnum=0
        for i in range(26):
            dic[chr(i+ord('A'))]=0
        l=0
        r=0
        ans=0
        while(r<len(s)):
            dic[s[r]]+=1
            maxnum=max(maxnum,max(dic.values()))
            r+=1
            if(r-l>maxnum+k):
                dic[s[l]]-=1
                l+=1
            ans=max(ans,r-l)
        return ans