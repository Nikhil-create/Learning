class ListNode:
    def __init__(self, key= 0,val=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = ListNode()
        self.latest = ListNode()
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.prev = prev 
        node.next = next

    def remove(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]



        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)