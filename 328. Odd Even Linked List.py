# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        odd=head
        even=head.next
        tail=even
        while(even.next!=None and even.next.next!=None):
            odd.next=even.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        if(even.next!=None):
            odd.next=even.next
            even.next=None
            odd=odd.next
            odd.next=tail
        else:
            odd.next=tail
        return head


