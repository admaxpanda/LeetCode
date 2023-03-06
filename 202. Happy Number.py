class Solution:
    def isHappy(self, n: int) -> bool:
        def getnew(x):
            ans=0
            while(x>0):
                ans+=(x%10)*(x%10)
                x//=10
            return ans
        d={}
        while(1):
            if(n==1):
                return 1
            if(n in d):
                return 0
            else:
                d[n]=1
            n=getnew(n)
            