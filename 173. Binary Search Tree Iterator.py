class BSTIterator:
    nums=[]
    cur=-1
    def __init__(self, root: Optional[TreeNode]):
        def find(node):
            if(node.left):
                find(node.left)
            self.num.append(node.val)
            if(node.right):
                find(node.right)
        find(root)
    def next(self) -> int:
        self.cur+=1
        return self.nums[self.cur]
    def hasNext(self) -> bool:
        return (len(self.nums)>self.cur)
        