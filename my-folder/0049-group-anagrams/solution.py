class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            group_dict[key].append(string)

        return list(group_dict.values())

        
