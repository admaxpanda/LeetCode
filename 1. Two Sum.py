class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            cur=target-nums[i]
            if(cur in map):
                return [i,map[cur]]
            map[nums[i]]=i