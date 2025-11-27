class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
    # in order for  stack[-1] to not go out of bounds, check if stack exists first
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        
