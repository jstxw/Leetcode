class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_number = float("inf") 
        max_profit = 0 

        for i in prices:
            if i < min_number: 
                min_number = i 
            elif i - min_number > max_profit: 
                max_profit = i - min_number
        return max_profit
                
        
