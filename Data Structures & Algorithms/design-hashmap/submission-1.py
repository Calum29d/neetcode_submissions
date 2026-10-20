class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(0, 0) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        newNode = ListNode(key, value)
        bucketHead = self.hashMap[key % 10000]
        cur = bucketHead.next

        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next

        newNode.next = bucketHead.next
        bucketHead.next = newNode
        

    def get(self, key: int) -> int:
        bucketHead = self.hashMap[key % 10000]
        cur = bucketHead.next

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        bucketHead = self.hashMap[key % 10000]
        cur = bucketHead.next
        prev = bucketHead

        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)