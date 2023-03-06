class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return max(nums)
        f=[]
        f.append(nums[0])
        f.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            f.append(max(f[i-1],f[i-2]+nums[i]))
        return f[len(nums)-1]