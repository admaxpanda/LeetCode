# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans=[]
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if(root==None):
            return 0
        def find(node,val):
            val.append(node.val)
            if(node.left):
                tmp=find(node.left,[])
                for i in tmp:
                    val.append(i+node.val)
            if(node.right):
                tmp=find(node.right,[])
                for i in tmp:
                    val.append(i+node.val)
            for i in val:
                self.ans.append(i)
            return val
        self.ans=[]
        find(root,[])
        print(self.ans)
        return sum(1 for i in self.ans if i==targetSum)