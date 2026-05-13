class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        prefix = [gain[0]]
        for i in range(1, len(gain)):
            prefix.append(prefix[-1] + gain[i])
        if max(prefix) < 0:
            return 0
         
            
        return max(prefix)
        
