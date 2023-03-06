# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        cnt=0
        while(p):
            cnt+=1
            p=p.next
        cnt=cnt//2
        for i in range(cnt):
            head=head.next
        return head