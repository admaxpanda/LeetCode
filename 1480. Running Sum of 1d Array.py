class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out=[]
        out.append(nums[0])
        for i in range(1,len(nums)):
            out.append(nums[i]+out[i-1])
        return out