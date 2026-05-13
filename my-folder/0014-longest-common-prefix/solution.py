class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return " "
        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]: 
                if i >= len(s) or s[i] != char:
                # i is based on first string not every string, hence, must accomodate for
                #words with length the same as strs[0]
                    return strs[0][:i]
        return strs[0]




