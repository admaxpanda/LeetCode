class Solution:
    m=0
    n=0
    def searchMatrix(self, matrix, target: int) -> bool:
        self.m=len(matrix)
        self.n=len(matrix[0])
        def getindex(x):
            return (x)//self.n,(x)%self.n
        l=0
        r=self.m*self.n-1
        while(r-l>1):
            x,y=getindex((r+l)//2)
            if(matrix[x][y]==target):
                return 1
            elif(matrix[x][y]>target):
                r=(r+l)//2
            else:
                l=(r+l)//2
        if(r<self.m*self.n):
            x,y=getindex(r)
            if(matrix[x][y]==target):
                return 1
        if(l<self.m*self.n-1):
            x,y=getindex(l)
            if(matrix[x][y]==target):
                return 1
        return 0
s=Solution()
print(s.searchMatrix([[1]],0))