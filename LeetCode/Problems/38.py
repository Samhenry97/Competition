class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):
            cur = ans[0]
            cnt = 1
            tmp = []
            for j in range(1, len(ans)):
                if ans[j] == cur:
                    cnt += 1
                else:
                    tmp.append(str(cnt))
                    tmp.append(cur)
                    cur = ans[j]
                    cnt = 1
            tmp.append(str(cnt))
            tmp.append(cur)
            ans = ''.join(tmp)
        return ans