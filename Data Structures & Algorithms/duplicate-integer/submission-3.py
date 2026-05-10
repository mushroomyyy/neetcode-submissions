class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        ans = set(nums)
        return not (len(ans) == len(nums))
        