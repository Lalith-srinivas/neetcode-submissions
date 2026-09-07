class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for current in strs:
            sorted_str=''.join(sorted(current))
            if sorted_str in result:
                result[sorted_str].append(current)
            else:
                result[sorted_str]=[current]
        return sorted(list(result.values()))