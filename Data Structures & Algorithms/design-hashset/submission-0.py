class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(0) for _ in range(10000)]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            bucketHead = self.hashSet[key % 10000]
            newNode = ListNode(key)
            
            newNode.next = bucketHead.next
            bucketHead.next = newNode


    def remove(self, key: int) -> None:
        bucketHead = self.hashSet[key % 10000]
        prev = bucketHead
        cur = bucketHead.next

        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def contains(self, key: int) -> bool:
        bucketHead = self.hashSet[key % 10000]
        cur = bucketHead.next
        
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)