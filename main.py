class Solution(object):
    def isAnagram(self, s, t):
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
    
    def containsDuplicate(self, nums):
        numbers = set()
        for elem in numbers:
            if elem in numbers:
                return True
            numbers.add(elem)
        return False


str_1 = "cbcdea"

str_2 = "cbcdea"

solution = Solution()

print(solution.isAnagram(str_1, str_2))
# assert solution.containsDuplicate(nums_1)
