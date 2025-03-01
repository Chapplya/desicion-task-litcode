from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for elem in strs:
            sort_s = ''.join(sorted(elem))
            anagrams[sort_s].append(elem)
        
        return list(anagrams.values())

settings = Solution()

strs = ["act","pots","tops","cat","stop","hat"]

print(settings.groupAnagrams(strs))