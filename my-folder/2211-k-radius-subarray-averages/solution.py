class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # between i - k and i + k
        
        avgs = list()
        
        for i in range(len(nums)):
            if i-k<0 or i+k>=len(nums): #at len(nums) is also invalid as 
                avgs.append(-1)
            else:
                if i-k == 0:
                    array_sum = prefix[i+k]
                else:
                    array_sum = prefix[i+k]-prefix[i-k-1]
                average = array_sum//(2*k + 1 )
                # not 2k+1
                avgs.append(average)
        return avgs 
            
