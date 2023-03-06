# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        cnt=0
        while(p):
            cnt+=1
            p=p.next
        if(cnt==1):
            return None
        if(cnt==n):
            return head.next
        p=head
        for i in range(cnt-n-1):
            p=p.next
        p.next=p.next.next
        return head