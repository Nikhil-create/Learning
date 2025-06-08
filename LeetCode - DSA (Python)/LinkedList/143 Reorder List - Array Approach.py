class ListNode:
    def __init__(self, val=0,next= None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self,head: ListNode) -> None:
        arr=[]
        curr,length = head,0

        # Store the Nodes in array
        while curr:
            arr.append(curr)
            curr,length= curr.next, length + 1

        left,right = 0 , length-1
        lastNode = head

        # Use 2 pointer approach to iterate through the array
        while left < right:
            arr[left].next = arr[right]
            left +=1

            if left==right:
                lastNode = arr[right]
                break

            arr[right].next = arr[left]
            right-=1

            lastNode = arr[left]

        # If lastNode exists points its next to None
        if lastNode:
            lastNode.next = None


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
s = Solution()
s.reorderList(l)

    