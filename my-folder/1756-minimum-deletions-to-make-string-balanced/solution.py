class Solution:
    def minimumDeletions(self, s: str) -> int:
        # balanced means no b can appear before a 
        # first idea: for each b that appears, check if there is an a after it and if so pop the b 
        # however, this is bad as it will not give the minimum amount
        # correct implementation, 
        # track, number of b seen so far and the number of a's after the b
        # core idea: if you see b, track it, but any a after the b will cause a conflict and you need to choose either to delete the a or all the other bs 
        b_count = 0
        deletions = 0 

        for char in s:
            if char == "b":
                b_count += 1 
            else:
                deletions = min(b_count, deletions + 1)
        return deletions


