class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1
        
        freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        freq_list = list()
        # be careful of the fact that sorting returns a tuple, in which we converted into a dict 
        #however, keys of the dict is still mapping to the original nums
        # freq_sorted[0] does not work because the keys are in a different order 
        #solution, do not convert to dict, keep in tuple


        for i in range(k):
            freq_list.append(freq_sorted[i][0])
        
        return freq_list
            

        
