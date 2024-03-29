class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def remove(self,node):
        prev=node.prev
        next=node.next

        prev.next=next
        next.prev=prev

    def insert(self,node):
        prev=self.right.prev
        next=self.right

        next.prev=node

        node.next=next
        node.prev=prev

        prev.next=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)