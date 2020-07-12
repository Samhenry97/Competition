class Solution:
    def isNumber(self, s: str) -> bool:
        def integer(x):
            try:
                int(x)
                return True
            except:
                return False
        
        def decimal(x):
            try:
                float(x)
                return True
            except:
                return False
        
        s = s.strip()
        if not all([c.isnumeric() or c in 'e-+.' for c in s]):
            return False
        if s.count('e') > 1:
            return False
        if 'e' in s:
            l, r = s.split('e')
            return decimal(l) and integer(r)
        else:
            return decimal(s)