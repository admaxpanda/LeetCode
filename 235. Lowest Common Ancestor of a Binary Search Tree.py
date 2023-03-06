# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pT=[root]
        qT=[root]
        pos=root
        while(pos!=p):
            if(pos.val>p.val):
                pT.append(pos.left)
                pos=pos.left
            else:
                pT.append(pos.right)
                pos=pos.right
        pos=root
        while(pos!=q):
            if(pos.val>q.val):
                qT.append(pos.left)
                pos=pos.left
            else:
                qT.append(pos.right)
                pos=pos.right
        ans=None
        lens=float('inf')
        i=len(pT)-1
        while(i>=0):
            k=len(qT)-1
            while(k>=0):
                if(len(qT)+len(pT)-i-k>=lens):
                    break
                if(pT[i]==qT[k]):
                    lens=len(qT)+len(pT)-i-k
                    ans=pT[i]
                    break
                k-=1
            i-=1
        return ans