from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        dicts = Counter(nums)
        sorted_dicts = sorted(dicts.keys(), key=lambda x: dicts[x], reverse=True)
        return sorted_dicts[:k]
        """
        count = Counter(nums)

        max_freq = max(count.values())
        freq_buckets = [[] for _ in range(max_freq + 1)]

        for num, freq in count.items():
            freq_buckets[freq].append(num)

        result = []
        for idx in range(max_freq, 0, -1):
            for elem in freq_buckets[idx]:
                result.append(elem)
                if len(result) == k:
                    return result


settings = Solution()

nums = [-9, -2, -3, -3]
k = 2

print(settings.topKFrequent(nums, k))
