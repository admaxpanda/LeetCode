class Solution:
    def checkValidGrid(self, grid) -> bool:
        d={}
        n=len(grid)
        for i in range(n):
            for k in range(n):
                d[grid[i][k]]=(i,k)
        if(d[0] != (0,0)):
            return False
        cur=d[0]
        for i in range(1,n*n):
            if(abs(cur[0]-d[i][0])==2 and abs(cur[1]-d[i][1])==1 or abs(cur[0]-d[i][0])==1 and abs(cur[1]-d[i][1])==2):
                cur=d[i]
            else:
                return False
        return True
s=Solution()
print(s.checkValidGrid([[0,3,6],[5,8,1],[2,7,4]]))