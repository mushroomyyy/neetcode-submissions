class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        for num in numbers:
            cur_val = numbers[l] + numbers[r]
            if cur_val == target:
                return [l+1,r+1]
            elif cur_val > target:
                r -= 1
            else:
                l += 1
        return []
        