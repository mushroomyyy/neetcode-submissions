class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 1

                while (num + length) in nums_set:
                    length += 1
                max_streak = max(length, max_streak)
        return max_streak



            

        