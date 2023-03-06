class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items())
        d=sorted(d,key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(d[i][0])
        return ans
s=Solution()
print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))