class Solution:
    def levelOrder(self, root):
        ans=[]
        def dfs(node,level):
            if(node==None):
                return
            if(len(ans)<=level):
                ans.append([])
            ans[level].append(node.val)
            dfs(node=node.left,level=level+1)
            dfs(node=node.right,level=level+1)
        dfs(root,0)
        return ans
s=Solution()