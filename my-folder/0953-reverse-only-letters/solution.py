class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # we have to turn the string into a list first because it is immutable 
        # we reverse if the value is alpha
        # if it is keep it in place and go next, if else, reverse
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            if not chars[left].isalpha():
                left += 1 
            elif not chars[right].isalpha():
                right -= 1 
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1 
                right -= 1
        return "".join(chars)
        
