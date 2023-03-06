# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find(self,root,l=float('-inf'),r=float('inf')):
        if root==None:
            return True
        if(root.val<=l or root.val>=r):
            return False
        if Solution.find(self,root.left,l,root.val)==False:
            return False
        if Solution.find(self,root.right,root.val,r)==False:
            return False
        return True

    def isValidBST(self, root) -> bool:
        return Solution.find(self,root)
