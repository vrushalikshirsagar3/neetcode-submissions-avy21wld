class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs.values():
                st.append(c)
            else:
                if st and st[-1] == pairs[c]:
                    st.pop()
                else:
                    return False
        return not st