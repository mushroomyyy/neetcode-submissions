class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            cur = s[r]

            if cur in char_map and char_map[cur] >= l:
                l = char_map[cur] + 1
            char_map[cur] = r
            max_len = max(max_len,r - l + 1)
        return max_len
