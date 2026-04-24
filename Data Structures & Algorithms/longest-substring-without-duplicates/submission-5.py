class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0 
        cnt = 0 
        seen = set ()
        while j != len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            cnt = max(cnt, len(seen))
            j += 1
        return cnt