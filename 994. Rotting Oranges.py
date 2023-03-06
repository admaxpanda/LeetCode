class Solution:
    def orangesRotting(self, grid) -> int:
        new=sum(1 for i in grid for k in i if(k==2))
        fresh=sum(1 for i in grid for k in i if(k==1))
        rot=0
        if(fresh==0):
            return 0
        s=[]
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if(grid[i][k]==2):
                    s.append((i,k))
        ans=0
        while(new!=0):
            for i in grid:
                print(i)
            print(s)
            new=0
            ans+=1
            news=[]
            for i in s:
                x=i[0]
                y=i[1]
                if(x>0 and grid[x-1][y]==1):
                    news.append((x-1,y))
                    new+=1
                    grid[x-1][y]=2
                if(y>0 and grid[x][y-1]==1):
                    news.append((x,y-1))
                    new+=1
                    grid[x][y-1]=2
                if(x<len(grid)-1 and grid[x+1][y]==1):
                    news.append((x+1,y))
                    new+=1
                    grid[x+1][y]=2
                if(y<len(grid[0])-1 and grid[x][y+1]==1):
                    news.append((x,y+1))
                    new+=1
                    grid[x][y+1]=2
            rot+=new
            s=news
        print(rot)
        if(rot<fresh):
            return -1
        return ans-1
s=Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))