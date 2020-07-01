class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        r = ['^']
        for i, c in enumerate(name):
            if i+1 < len(name) and c == name[i+1]:
                r.append(c)
            else:
                r.append(c + '+')
        r.append('$')
        return re.match(''.join(r), typed)