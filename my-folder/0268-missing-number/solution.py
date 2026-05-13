class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        if sorted_nums[0] != 0:
            return 0 
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i-1] != 1:
                return sorted_nums[i-1] + 1 
            
        return len(nums)
