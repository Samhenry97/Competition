class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        found = {}
        for i in range(n):
            s = str(cells)
            if s in found:
                loop = i - found[s]
                return self.prisonAfterNDays(cells, (n - i) % loop)
            else:
                found[s] = i
                tmp = [0] * 8
                for i in range(1, 7):
                    tmp[i] = int(cells[i-1] == cells[i+1])
                cells = tmp
        return cells