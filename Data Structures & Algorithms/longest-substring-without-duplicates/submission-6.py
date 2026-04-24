class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        cnt = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, 1 + seen[s[r]])
            seen[s[r]] = r
            cnt = max(cnt, r - l + 1)
        return cnt