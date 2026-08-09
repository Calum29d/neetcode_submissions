class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = [] #hold the times taken to get to target

        for p, s in sorted(cars)[::-1]: #iterate in reverse sorted order
            stack.append((target - p) / s)
            
            #possible collision and then check if the there has been a collision/fleet made
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        #O(nlogn) time and O(n) space