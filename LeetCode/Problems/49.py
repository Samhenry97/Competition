from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(lambda: [])
        for s in strs:
            key = ''.join(sorted(list(s)))
            mp[key].append(s)
        ans = []
        for k in mp.keys():
            ans.append(mp[k])
        return ans