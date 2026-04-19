class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapOfChars = {")" : "(", "]" : "[", "}" : "{"}

        if len(s)%2 != 0:
            return False #if len of string is not even then that means a bracket is not closed so can automatically return false

        #this is my thought, the last opened bracket must be the first one to be closed.

        for char in s:
            if char not in mapOfChars:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif mapOfChars[char] == stack[-1]:
                    stack.pop()
                else:
                    return False








                

        if not stack:
            return True
        else:
            return False
        

            




        

        
        