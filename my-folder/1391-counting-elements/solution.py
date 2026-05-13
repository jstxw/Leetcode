class Solution:
    def countElements(self, arr: List[int]) -> int:
        j = 0 
        seen = set(arr)
        for i in arr:
            if (i+1) in seen: 
                j += 1
            seen.add(i)
        return j
        
