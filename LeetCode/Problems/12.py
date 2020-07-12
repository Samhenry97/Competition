class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        m, num = divmod(num, 1000)
        ans.append('M' * m)
        if num // 100 == 9:
            ans.append('CM')
            num -= 900
        d, num = divmod(num, 500)
        ans.append('D' * d)
        if num // 100 == 4:
            ans.append('CD')
            num -= 400
        c, num = divmod(num, 100)
        ans.append('C' * c)
        if num // 10 == 9:
            ans.append('XC')
            num -= 90
        l, num = divmod(num, 50)
        ans.append('L' * l)
        if num // 10 == 4:
            ans.append('XL')
            num -= 40
        x, num = divmod(num, 10)
        ans.append('X' * x)
        if num == 9:
            ans.append('IX')
            num -= 9
        v, num = divmod(num, 5)
        ans.append('V' * v)
        if num == 4:
            ans.append('IV')
            num -= 4
        ans.append('I' * num)
        return ''.join(ans)