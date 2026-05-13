class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(lo, hi, condition):  
            while lo<=hi: 
                mid = (lo + hi)//2
                result = condition(mid)
        
                if result == 'left':
                    hi = mid -1 
                elif result == 'right':
                    lo = mid + 1 
                elif result == 'found':
                    return mid 
            return -1 
        

        def first_position():
            def condition(mid):
                if nums[mid] == target: 
                    if mid > 0 and nums[mid -1 ]== target: 
                        return 'left'
                    else:
                        return 'found'
                    
                elif nums[mid] > target: 
                    return 'left'
                else: 
                    return 'right'
            return binary_search(0,len(nums)-1, condition)

        def last_position():
            def condition (mid):
                if nums[mid] == target: 
                    if mid <len(nums)-1 and nums[mid + 1 ]== target: 
                        return 'right'
                    else:
                        return 'found'
                    
                elif nums[mid] < target: 
                    return 'right'
                else: 
                    return 'left'
            return binary_search(0,len(nums)-1, condition)


        return [first_position(), last_position()]
                
            
            
