class Solution:
    def climbStairs(self, n: int) -> int:
        f=[]
        f.append(0)
        f.append(1)
        f.append(2)
        f.append(3)
        for i in range(4,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
