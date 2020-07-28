class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = sorted([(v, k) for k, v in c.items()], reverse=True)
        return [ans[i][1] for i in range(k)]
            