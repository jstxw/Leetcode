class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0 
        for i in range(k):
            sum += nums[i]
            average = sum/k
            
        ans = average
        
        for x in range(k, len(nums)):
            sum += nums[x] - nums[x-k]
            average = sum/k
            ans = max(ans, average)
        return ans 
        
        
        
        
        
