class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_2 = list(enumerate(nums))
        num_2.sort(key=lambda x:x[1])

        left, right = 0, len(num_2) - 1

        while left < right: 
            current_sum = num_2[left][1] + num_2[right][1] 
            if current_sum == target: 
                return [num_2[left][0], num_2[right][0]]
            else:
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
        return

