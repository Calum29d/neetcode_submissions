class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # I think its a stack problem

        stack = []

        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)

            elif op == "D":
                num = stack[-1]
                stack.append(num * 2)

            else:
                stack.append(int(op))
        
        return sum(stack)
        
        
        