# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def find(l,r,nums):
            mid=(l+r)//2
            node=TreeNode(val=nums[mid])
            if(mid>l):
                node.left=find(l,mid-1,nums)
            if(mid<r):
                node.right=find(mid+1,r,nums)
            return node
        return find(0,len(nums)-1,nums)
s=Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))