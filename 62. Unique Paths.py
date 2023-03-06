class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f=[]
        for i in range(m):
            f.append([])
            for k in range(n):
                f[i].append(1)
        for i in range(1,m):
            for k in range(1,n):
                f[i][k]=f[i-1][k]+f[i][k-1]
        return f[m-1][n-1]
s=Solution()
print(s.uniquePaths(3,7))