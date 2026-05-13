class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s_under = s.lower()
        s_under_a = "".join(ch for ch in s_under if ch.isalnum())

        left, right = 0, len(s_under_a) - 1 

        while left < right: 
            if s_under_a[left] != s_under_a[right]:
                print("false")
                return False
            else: 
                left += 1
                right -= 1 
                print("true")
        return True

        
