class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        n = len(nums)
        for arr in nums:
            for x in arr: 
                dic[x] += 1
        ans = []
        for y in dic:
            if dic[y] == n:
                ans.append(y)
        
        return sorted(ans)
        

        
