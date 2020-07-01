class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        def works(cnt):
            pref = strs[0][:cnt]
            for s in strs:
                if not s.startswith(pref):
                    return False
            return True
        
        bot, top = 0, min([len(s) for s in strs])
        while bot <= top:
            mid = (bot + top) // 2
            if works(mid):
                bot = mid + 1
            else:
                top = mid - 1
        return strs[0][:(bot + top) // 2]