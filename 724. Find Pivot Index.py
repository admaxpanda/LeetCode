class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right=sum(nums)-nums[0]
        left=0
        if(right==0):
            return 0
        for i in range(1,len(nums)):
            right-=nums[i]
            left+=nums[i-1]
            if(right==left):
                return i
        return -1
        