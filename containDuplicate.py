from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for elem in strs:
            sort_s = "".join(sorted(elem))
            anagrams[sort_s].append(elem)

        return list(anagrams.values())

    def containsDuplicate(self, nums):
        numbers = set()
        for elem in numbers:
            if elem in numbers:
                return True
            numbers.add(elem)
        return False

    def isAnagram_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts = [0] * 26
        for char in s:
            dicts[ord(char) - ord("a")] += 1
        for chars in t:
            dicts[ord(chars) - ord("a")] -= 1
        for m in dicts:
            if m != 0:
                return False
        return True

    def isAnagram_2(self, s, t):
        num_to_idx_1 = Counter(s)
        for elem in t:
            if elem not in num_to_idx_1:
                return False
            num_to_idx_1[elem] -= 1
            if num_to_idx_1[elem] == 0:
                del num_to_idx_1[elem]
        return not num_to_idx_1

    def twoSum(self, nums, target):
        num_to_idx = {}
        for index, elem in enumerate(nums):
            diff = target - elem
            if diff in num_to_idx:
                return [index, num_to_idx[diff]]
            num_to_idx[elem] = index


solution = Solution()
