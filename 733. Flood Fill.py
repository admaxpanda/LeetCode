from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        c=image[sr][sc]
        if(c==color):
            return image
        q=deque()
        q.append((sr,sc))
        while(q):
            p=q.popleft()
            x=p[0]
            y=p[1]
            image[x][y]=color
            if(x>0 and image[x-1][y]==c):
                q.append((x-1,y))
            if(y>0 and image[x][y-1]==c):
                q.append((x,y-1))
            if(x<len(image)-1 and image[x+1][y]==c):
                q.append((x+1,y))
            if(y<len(image[0])-1 and image[x][y+1]==c):
                q.append((x,y+1))
        return image
s=Solution()
print(s.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))