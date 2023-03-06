class Solution:
    def findAnagrams(self, s: str, p: str) -> int:
        if(len(p)>len(s)):
            return []
        dic={}
        tar={}
        ans=[]
        for i in range(26):
            dic[chr(i+ord('a'))]=0
            tar[chr(i+ord('a'))]=0
        for i in p:
            dic[i]+=1
        for i in range(len(p)):
            tar[s[i]]+=1
        if(tar==dic):
            ans.append(0)
        for i in range(len(p),len(s)):
            tar[s[i-len(p)]]-=1
            tar[s[i]]+=1
            if(tar==dic):
                ans.append(i-len(p)+1)
        return ans
s=Solution()
print(s.findAnagrams(s = "cbaebabacd", p = "abc"))