class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        rem = n % k
        ans = [s[:rem]] if rem else []
        for i in range(rem, n, k):
            ans.append(s[i:i+k])
        return '-'.join(ans)
        