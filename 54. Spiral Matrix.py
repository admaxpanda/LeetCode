class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        cnt=0
        tot=m*n
        cur=0
        x=0
        y=0
        while(cnt<tot):
            if(matrix[x][y]!=-200):
                cnt+=1
                ans.append(matrix[x][y])
            matrix[x][y]=-200
            if(cur==0):
                if(y<n-1 and matrix[x][y+1]!=-200):
                    y+=1
                else:
                    cur=1
            if(cur==1):
                if(x<m-1 and matrix[x+1][y]!=-200):
                    x+=1
                else:
                    cur=2
            if(cur==2):
                if(y>0 and matrix[x][y-1]!=-200):
                    y-=1
                else:
                    cur=3
            if(cur==3):
                if(x>0 and matrix[x-1][y]!=-200):
                    x-=1
                else:
                    cur=0
        return ans
s=Solution()
print(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))