class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace={}
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            if(s[i] not in replace):
                if(t[i] in replace.values()):
                    return False
                replace[s[i]]=t[i]
            else:
                if(replace[s[i]]!=t[i]):
                    return False
        return True
s=Solution()
print(s.isIsomorphic(s='paper',t='title'))