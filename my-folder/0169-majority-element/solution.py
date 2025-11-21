class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq.keys():
                freq[i] = 1 
            else:
                freq[i] += 1
        
        most_common = max(freq, key=freq.get)
        return most_common
