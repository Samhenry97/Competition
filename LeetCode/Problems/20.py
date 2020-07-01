class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '{([':
                st.append(c)
            elif len(st) == 0:
                return False
            else:
                if c == ']' and st[-1] != '[' or c == ')' and st[-1] != '(' or c == '}' and st[-1] != '{':
                    return False
                st.pop()
        return len(st) == 0