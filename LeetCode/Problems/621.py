class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        most = freq.most_common()[0][1]
        found = sum([freq[key] == most for key in freq])
        return max(len(tasks), (most - 1) * (n + 1) + found)