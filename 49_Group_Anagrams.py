#Input: strs = ["eat","tea","tan","ate","nat","bat"]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            anagram[key].append(i)
        return list(anagram.values())