from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
            
        hash_map = {}
        curr = head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hash_map[curr].next = hash_map.get(curr.next)
            hash_map[curr].random = hash_map.get(curr.random)
            curr = curr.next

        return hash_map[head]