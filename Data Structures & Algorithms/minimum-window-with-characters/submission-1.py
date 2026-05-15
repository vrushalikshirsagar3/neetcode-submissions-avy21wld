class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for ch in t:
            freq_t[ch] = 1 + freq_t.get(ch, 0)
        have = 0 
        need = len(freq_t)
        left = 0
        min_seq = ''
        curr_seq = ''
        window = {}
        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)
            #increment have
            if ch in freq_t and window[ch] == freq_t[ch]:
                have += 1
            while have == need:
                curr_seq = s[left: right + 1]
                if min_seq == '' or len(min_seq) > len(curr_seq):
                    min_seq = curr_seq
                #remove characters from left
                if s[left] in freq_t:
                    window[s[left]] -= 1
                #decrement have if count of left character in window < count lef character in freq_t
                if s[left] in freq_t and window[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        return min_seq