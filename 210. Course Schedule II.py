import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        e=[]
        for i in range(numCourses):
            e.append([])
        for i in prerequisites:
            e[i[1]].append(i[0])
        q=queue.PriorityQueue()
        for i in range(numCourses):
            q.put((len(e[i]),i))
        ans=[]
        while(not q.empty()):
            cur=q.get()
            if(cur[0]==0):
                ans.append(cur[1])
            else:
