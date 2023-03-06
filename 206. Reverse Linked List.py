# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        s=[]
        while(head):
            s.append(head)
            head=head.next
        tail=p=ListNode()
        
        while(s):
            tmp=s.pop()
            p.next=tmp
            p=p.next
        p.next=None
        return tail.next
a=ListNode(5,None)
b=ListNode(4,a)
c=ListNode(3,b)
d=ListNode(2,c)
e=ListNode(1,d)
s=Solution()
ans=s.reverseList(head=e)
while(ans):
    print(ans.val)
    ans=ans.next