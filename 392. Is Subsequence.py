class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        i=0
        while(k<len(t) and i<len(s)):
            if(t[k]==s[i]):
                i+=1
            k+=1
        if(i==len(s)):
            return True
        return False
s=Solution()
print(s.isSubsequence(s='abc',t='ahbgdc'))