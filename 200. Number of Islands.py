class Solution:
    def numIslands(self, grid):
        def dfs(x,y,num):
            grid[x][y]=str(num)
            if(x>0 and grid[x-1][y]=='1'):
                dfs(x-1,y,num)
            if(y>0 and grid[x][y-1]=='1'):
                dfs(x,y-1,num)
            if(x<len(grid)-1 and grid[x+1][y]=='1'):
                dfs(x+1,y,num)
            if(y<len(grid[0])-1 and grid[x][y+1]=='1'):
                dfs(x,y+1,num)
        ans=0
        
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if(grid[i][k]=='1'):
                    ans+=1
                    dfs(i,k,ans+1)
        return ans
s=Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))