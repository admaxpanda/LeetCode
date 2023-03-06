class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f=[]
        f.append(0)
        f.append(0)
        for i in range(2,len(cost)+1):
            f.append(min(f[i-1]+cost[i-1],f[i-2]+cost[i-2]))
        return f[len(cost)]