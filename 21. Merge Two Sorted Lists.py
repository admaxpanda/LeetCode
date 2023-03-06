class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head=ListNode(0,None)
        if(list1==None and list2==None):
            return None
        elif (list1==None):
            return list2
        elif (list2==None):
            return list1
        else:
            if(list1.val<list2.val):
                head=list1
                list1=list1.next
            else:
                head=list2
                list2=list2.next
        now=head
        while(list1!=None and list2!=None):
            if(list1.val<list2.val):
                now.next=list1
                now=list1
                list1=list1.next
            else:
                now.next=list2
                now=list2
                list2=list2.next
        if(list1!=None):
            while(list1!=None):
                now.next=list1
                now=list1
                list1=list1.next
        elif(list2!=None):
            while(list2!=None):
                now.next=list2
                now=list2
                list2=list2.next
        return head
a=ListNode(4,None)
b=ListNode(2,a)
c=ListNode(1,b)

d=ListNode(4,None)
e=ListNode(3,d)
f=ListNode(1,e)
s=Solution()
ans=s.mergeTwoLists(c,f)
while(ans!=None):
    print(ans.val)
    ans=ans.next