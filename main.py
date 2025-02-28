class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


nums_1 = [1, 2, 3, 4]

nums_2 = [1, 2, 2, 3, 4]

solution = Solution()

print(solution.containsDuplicate(nums_1))
print(solution.containsDuplicate(nums_2))
