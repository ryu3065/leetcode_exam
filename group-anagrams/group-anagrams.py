class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_str = {}
        for i, s in enumerate(strs):
            
            sorted_str = ''.join(sorted(s))
            
            if sorted_str in group_str:
                group_str[sorted_str].append(s)
            else:
                group_str[sorted_str] = [s]
            
        return list(group_str.values())
        
        