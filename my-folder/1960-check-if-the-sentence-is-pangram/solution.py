class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letters = {ch for ch in sentence.lower() if ch.isalpha()} 
        return len(letters) == 26
            
        
