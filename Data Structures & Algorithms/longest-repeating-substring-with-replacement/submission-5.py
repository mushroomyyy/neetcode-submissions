class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            #add each char's count
            count[s[r]] = 1 + count.get(s[r],0)
            #always count our max for ans
            max_freq = max(max_freq, count[s[r]])
            #while we hit > k
            while (r - l + 1) - max_freq > k:
                #we minus 1 from the dup of the char
                count[s[l]] -= 1
                #then we shift the l pointer forward
                l += 1
            
            max_len = max(max_len, r- l +1)
        return max_len
            
        