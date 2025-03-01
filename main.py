class Solution(object):
    def containsDuplicate(self, nums):
        sets = set()
        for elem in nums:
            if elem in sets:
                return True
            else:
                sets.add(elem)
        return False


nums_1 = [1, 2, 3, 4]

nums_2 = [1, 2, 2, 3, 4]

solution = Solution()

print(solution.containsDuplicate(nums_1))
print(solution.containsDuplicate(nums_2))
