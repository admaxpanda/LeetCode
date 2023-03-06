class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        minlen=float('inf')
        if(len(strs)==0):
            return ans
        for i in strs:
            minlen=min(minlen,len(i))
        for i in range(minlen):
            tag=1
            ch=strs[0][i]
            for k in range(1,len(strs)):
                if(strs[k][i]!=ch):
                    tag=0
                    return ans
            if(tag):
                ans+=ch
        return ans