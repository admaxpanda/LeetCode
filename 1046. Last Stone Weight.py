import queue
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        q=queue.PriorityQueue()
        for i in stones:
            q.put(-i)
        while(not q.empty()):
            a=q.get()
            if(q.empty()):
                return -a
            b=q.get()
            print(a,' ',b)
            if(a!=b):
                q.put(-abs(a-b))
        if(q.empty()):
            return 0
        return -q.get()
s=Solution()
print(s.lastStoneWeight([2,2]))