class Solution(object):
    def containsDuplicate(self, nums):
        numbers = set()
        for elem in numbers:
            if elem in numbers:
                return True
            numbers.add(elem)
        return False


nums_1 = [1, 2, 3, 4]

nums_2 = [1, 2, 2, 3, 4]

solution = Solution()

# assert solution.containsDuplicate(nums_1)
