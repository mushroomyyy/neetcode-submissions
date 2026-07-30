class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #whether if the character is a duplicate in the window
        char_map = {}
        # l pointer
        l = 0
        # cur count
        longest = 0
        for r in range(len(s)):
            # if the right most value is already in the map -> duplicate and 
            if s[r] in char_map and char_map[s[r]] >= l :
                l = char_map[s[r]] + 1
            char_map[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest

        