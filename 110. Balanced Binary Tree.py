# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans=1
    def isBalanced(self, root: TreeNode) -> bool:
        if(root==None):
            return 1
        def finddepth(node):
            depthL=0
            depthR=0
            if(node.left or node.right):
                if(node.left):
                    depthL=finddepth(node.left)
                if(node.right):
                    depthR=finddepth(node.right)
            if(abs(depthL-depthR)>1):
                self.ans=0
            return max(depthR,depthL)+1
        finddepth(root)
        return self.ans
s=Solution()
print(s.isBalanced(TreeNode(1)))
        # l=[]
        # def findleaves(node,depth):
        #     if(node.left and node.right):
        #         findleaves(node.left,depth+1)
        #         findleaves(node.right,depth+1)
        #     else:
        #         l.append(depth)
        #         if(node.left):
        #             findleaves(node.left,depth+1)
        #         if(node.right):
        #             findleaves(node.right,depth+1)
        # findleaves(root,0)
        # if(max(l) - min(l)>1):
        #     return 0
        # return 1
