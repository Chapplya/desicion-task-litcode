from collections import Counter


class Solution(object):
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
        dict_1 = Counter(s)
        dict_2 = Counter(t)
        return dict_1 == dict_2


solution = Solution()


solution = Solution()
