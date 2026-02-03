class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:   
        def build(s):
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                elif stack: #check the stack is not empty firs
                    stack.pop() 
            return "".join(stack)
        return build(s) == build(t)



            
