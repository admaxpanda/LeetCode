import math
class Solution:
    def repairCars(self, ranks, cars) -> int:
        ans=0
        l=0
        r=1000000000000000
        n=len(ranks)
        while(l<=r):
            mid=(l+r)//2
            cnt=0
            for i in ranks:
                cnt+=(int)(math.sqrt(mid//i))
            if(cnt>=cars):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
s=Solution()
print(s.repairCars([4,2,3,1],10))

