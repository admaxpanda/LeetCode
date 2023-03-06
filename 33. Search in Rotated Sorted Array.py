class Solution:
    pos=0
    length=0
    def search(self, nums: list[int], target: int) -> int:
        self.length=len(nums)
        l=0
        r=self.length-1
        while(r-l>1):
            if(nums[r]>nums[l]):
                r=l
                break
            if(nums[(r+l)//2]>nums[l]):
                l=(r+l)//2
            elif(nums[(r+l)//2]<nums[l]):
                r=(r+l)//2
            else:
                break
        self.pos=r
        def getindex(x):
            return (x+self.pos)%self.length
        l=0
        r=self.length-1
        while(r-l>1):
            i=getindex((r+l)//2)
            if(nums[i]>target):
                r=(r+l)//2
            elif(nums[i]<target):
                l=(r+l)//2
            else:
                return i
        i=getindex(r)
        if(nums[i]==target):
            return i
        i=getindex(l)
        if(nums[i]==target):
            return i
        return -1
s=Solution()
print(s.search([1,3,5],5))