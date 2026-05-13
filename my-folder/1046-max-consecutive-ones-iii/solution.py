class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = current = 0 
        for right in range(len(nums)):
            if nums[right] == 0:
                current += 1 
            
                while current > k:
                    if nums[left] == 0:
                        current -= 1
                    left += 1
            
            ans = max(ans, right - left + 1)
        return ans
