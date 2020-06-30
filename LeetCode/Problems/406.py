class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people) 
        ans = [0] * n
        people.sort()
        for i, p in enumerate(people) :
            cnt = 0
            for j in range(n):
                if cnt >= p[1] and ans[j] == 0:
                    ans[j] = p
                    break
                if ans[j] == 0 or ans[j][0] >= p[0]:
                    cnt += 1
        return ans