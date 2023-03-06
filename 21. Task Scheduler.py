import collections
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        d = collections.Counter(tasks)
        s=sorted(d.values(),reverse=True)
        ans=(s[0]-1)*(n+1)+sum(1 for i in s if i==s[0])
        return max(ans,len(tasks))
s=Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
