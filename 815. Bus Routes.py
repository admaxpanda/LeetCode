import queue
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if(target==source):
            return 0
        dis=[]
        for i in range(len(routes)):
            dis.append([])
            for k in range(len(routes)):
                dis[i].append(0)
        for i in range(len(routes)):
            for k in range(i+1,len(routes)):
                if(set(routes[i]) & set(routes[k])):
                    dis[i][k]=dis[k][i]=1
        q=queue.Queue()
        inqueue=[]
        for i in range(len(routes)):
            inqueue.append(0)
        for i in range(len(routes)):
            if(source in routes[i]):
                q.put((i,1))
                inqueue[i]=1
        while(not q.empty()):
            cur=q.get()
            if(target in routes[cur[0]]):
                return cur[1]
            for i in range(len(routes)):
                if(inqueue[i]==0 and dis[cur[0]][i]==1):
                    inqueue[i]=1
                    q.put((i,cur[1]+1))
        return -1
