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


nums_1 = "cbcdea"

nums_2 = "cbcdea"

solution = Solution()

print(solution.isAnagram(nums_1, nums_2))
