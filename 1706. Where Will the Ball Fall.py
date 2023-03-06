class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m=len(grid)
        n=len(grid[0])
        ans=[]
        for i in range(n):
            forward='up'
            x=0
            y=i
            while(1):
                if(x==m):
                    ans.append(y)
                    break
                if(grid[x][y]==1):
                    if(forward=='up'):
                        if(y==n-1):
                            ans.append(-1)
                            break
                        forward='left'
                        y+=1
                    elif(forward=='left'):
                        if(x==m-1):
                            ans.append(y)
                            break
                        forward='up'
                        x+=1
                    elif(forward=='right'):
                        ans.append(-1)
                        break
                elif(grid[x][y]==-1):
                    if(forward=='up'):
                        if(y==0):
                            ans.append(-1)
                            break
                        forward='right'
                        y-=1
                    elif(forward=='right'):
                        if(x==m-1):
                            ans.append(y)
                            break
                        forward='up'
                        x+=1
                    elif(forward=='left'):
                        ans.append(-1)
                        break
        return ans
s=Solution()
print(s.findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))