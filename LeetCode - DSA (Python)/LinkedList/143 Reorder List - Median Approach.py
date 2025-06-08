class ListNode:
    def __init__(self, val=0,next= None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self,head: ListNode) -> None:

        # Don't run this if head is None
        if not head:
            return None

        fast,slow = head, head 

        # Find the mid of the LinkedList
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # create 2 seprate LinkedList till mid call it first and after mid call is second
        second = slow.next
        slow.next = None
        first = head

        # reverse the second linked list
        node = None
        while second:
            temp = second.next
            second.next = node 
            node = second
            second = temp

        second = node 

        # Zig zag traversal
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1 
            first = temp1
            second = temp2

            


