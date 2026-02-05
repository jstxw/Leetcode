class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums) # to mimic circular behavior
        result = []
        for i in range(len(nums)):
            if nums[i] > 0: 
                d = nums[i]
                result.append(nums[(i + d)%n]) #index out of range
            elif nums[i] < 0:
                d = abs(nums[i])
                result.append(nums[(i-d)%n])
            else:
                result.append(nums[i])
        return result
