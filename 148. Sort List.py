# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if(head==None):
            return head
        n=[]
        p=head
        while(p!=None):
            n.append(p.val)
            p=p.next
        n.sort()
        h=ListNode(val=n[0],next=None)
        p=h
        for i in range(1,len(n)):
            tmp=ListNode(val=n[i],next=None)
            p.next=tmp
            p=tmp
        return h

s=Solution()
a=ListNode(3)
b=ListNode(1,a)
c=ListNode(2,b)
d=ListNode(4,c)
print(s.sortList(d))