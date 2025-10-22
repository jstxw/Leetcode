class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        freq = defaultdict(int)
        for i in s: 
            freq[i] += 1

        frequencies = freq.values()
        return len(set(frequencies)) == 1
        
        
