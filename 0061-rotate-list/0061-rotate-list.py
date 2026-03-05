# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length=1
        temp=head
        while temp.next:
            temp=temp.next
            length+=1

        k=k%length
        temp.next=head
        steps=length-k
        new_tail=head

        for _ in range(steps-1):
            new_tail=new_tail.next


        new_head=new_tail.next
        new_tail.next=None

        return new_head    

       

        temp2.next=head
        return temp.next       
        