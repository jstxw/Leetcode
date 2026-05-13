#the idea is that we analyze each pair indivdually 
# we find out the possible results or sums pairs can have, and then find the overlap of those pairs
#ie if a pair is 1,3 with limit 4, then keeping 1,(1...4) = 2....5
#and keeping 3: keeping 3, (1...4) = 4...7
#so range is 2...7
# with 4 being 0 moves and 2-7 without 4 being 1 move 

from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # diff[target] stores cost changes at that target sum
        # possible target sums are from 2 to 2 * limit
        diff = [0] * (2 * limit + 2)

        # analyze each mirrored pair
        for i in range(n // 2): #bc of pairs, a is the first, b is the last 
            a = nums[i]
            b = nums[n - 1 - i]

            # current sum costs 0 moves
            current_sum = a + b 

            # target sums reachable with 1 move
            low = min(a, b) + 1 
            high = max(a, b) + limit

            # assume every target sum costs 2 moves
            diff[2] += 2 # differential array, so 2 for all indexs

            # from low to high, cost becomes 1 instead of 2
            diff[low] -= 1
            diff[high + 1] += 1

            # at current_sum, cost becomes 0 instead of 1
            diff[current_sum] -= 1
            diff[current_sum + 1] += 1

        answer = float("inf")
        moves = 0

        # prefix sum over diff to get real cost for each target sum
        for target in range(2, 2 * limit + 1):
            moves += diff[target]
            answer = min(answer, moves)

        return answer



        
