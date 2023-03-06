# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        s=[]
        s.append(root)
        while(len(s)):
            p=s.pop()
            if(p==None):
                continue
            tmp=p.left
            p.left=p.right
            p.right=tmp
            s.append(p.left)
            s.append(p.right)
        return root