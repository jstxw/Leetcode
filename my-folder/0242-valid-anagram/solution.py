from collections import Counter # import a counter 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        if s_dict == t_dict: 
            return True

        else:
            return False
