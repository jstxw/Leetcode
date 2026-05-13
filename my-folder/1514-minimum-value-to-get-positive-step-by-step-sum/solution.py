class Solution:
    def minStartValue(self, nums: List[int]) -> int:
                
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        
        minimum = min(prefix_sum)
        
        if minimum < 1: 
            startValue = 1- minimum 
        else:
            startValue = 1
        return startValue

            
        
