class ListNode:
    def __init__(self, val, nxt):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = self.size = 0
        self.maxSize = k
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.q[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.maxSize # wrap around function
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.size -= 1
        self.head = (self.head + 1) % self.maxSize
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.size == 0: return True
        return False

    def isFull(self) -> bool:
        if self.size == self.maxSize: return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()