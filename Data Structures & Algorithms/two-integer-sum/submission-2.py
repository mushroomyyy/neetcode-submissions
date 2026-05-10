class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h_dict = dict()
        for i in range(n):
            diff = target - nums[i]
            if diff in h_dict:
                return [h_dict[diff], i]
            else:
                h_dict[nums[i]] = i
        return []

        