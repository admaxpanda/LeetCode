class Solution:
    def evenOddBit(self, n: int):
        ans=[0,0]
        if(n==0):
            return [0,1]
        i=0
        while(n>0):
            if(n%2):
                ans[i%2]+=1
            i+=1
            n//=2
        return ans
s=Solution()
print(s.evenOddBit(2))
