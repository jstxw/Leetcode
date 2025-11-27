class Solution:
    def makeGood(self, s: str) -> str:
        
        """
        implementation:
        we first have to turn the immutable string into a list
        after, just make sure the two cases work
        mistake: at first, i was checking through s_list[i-1] and s_list[i+1]
        this is bad as we have to deal with going out of bounds
        """
        stack = []
        s_list = list(s)
        for i in range(len(s_list)):
            ch = s_list[i] #make sure to have this 
            # if current is lower, previous is upper of the same letter
            if stack and stack[-1].isupper() and stack[-1].lower() == ch:
                stack.pop()
            # if current is upper, previous is lower of the same letter
            elif stack and ch.isupper() and ch.lower() == stack[-1]:
                stack.pop()
            else: 
                stack.append(ch)
        return "".join(stack)
            
