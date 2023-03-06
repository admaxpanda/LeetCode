# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q=[]
        p=head
        while(p):
            q.append(p.val)
            p=p.next
        for i in range(len(q)//2):
            if(q[i]!=q[len(q)-1-i]):
                return 0
        return 1