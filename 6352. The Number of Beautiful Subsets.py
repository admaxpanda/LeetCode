class Solution:
    ans=0
    def beautifulSubsets(self, nums, k: int) -> int:
        nums.sort()
        length=len(nums)
        vis=[0]*1001
        # print(pair)
        def binarysearch(i,cur,length,vis,nums):
            if(i in cur):
                # print(cur)
                self.ans+=1
            if(i+1<length):
                
                if(nums[i+1]-k<0 or vis[nums[i+1]-k]==0):
                    vis[nums[i+1]]=1
                    binarysearch(i+1,cur+[i+1],length,vis,nums)
                    vis[nums[i+1]]=0
                binarysearch(i+1,cur,length,vis,nums)
        vis[nums[0]]=1
        binarysearch(0,[0],length,vis,nums)
        vis[nums[0]]=0
        binarysearch(0,[],length,vis,nums)
        return self.ans
s=Solution()
print(s.beautifulSubsets([2,4,6],2))