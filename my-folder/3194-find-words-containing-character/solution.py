class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        results = []

        for i in range(len(words)):
            if x in words[i]:
                results.append(i)
                # break 
        return results
        #     elif x not in words[i]:
        # i+=1 
            
