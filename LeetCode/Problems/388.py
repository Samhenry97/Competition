class Solution:
    def lengthLongestPath(self, input: str) -> int:
        data = input.split('\n')
        st, ans = [], 0
        for part in data:
            file = part.lstrip('\t')
            level = len(part) - len(file)
            while len(st) and level < len(st):
                st.pop()
            st.append(file)
            if '.' in file:
                ans = max(ans, sum([len(x) for x in st]) + len(st) - 1)
        return ans