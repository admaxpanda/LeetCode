# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return None
        def find(node):
            depthL=0
            depthR=0
            if(node.left):
                depthL=find(node.left)
            if(node.right):
                depthR=find(node.right)
            self.ans=max(self.ans,depthL+depthR)
            return max(depthR,depthL)+1
        find(root)
        return self.ans