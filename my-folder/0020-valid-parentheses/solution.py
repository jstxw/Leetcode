class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"{": "}", "[": "]", "(": ")"}

        for i in s:
            if i in matching:
                stack.append(i)
            else:
                if not stack:
                    return False 
            
                previous_opening = stack.pop()
                # If previous_opening is "(", then matching[previous_opening] returns ")"
                if matching[previous_opening] != i:
                    return False
        return not stack

        # only valid if the stack is empty 

        
