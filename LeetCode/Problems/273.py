class Solution:
    def __init__(self):
        self.ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.thou = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
    
    def section(self, num: int) -> str:
        ans = []
        hun, ten = divmod(num, 100)
        if hun:
            ans.append(self.ones[hun])
            ans.append('Hundred')
        if ten >= 20:
            ten, one = divmod(ten, 10)
            ans.append(self.tens[ten])
            if one:
                ans.append(self.ones[one])
        else:
            ans.append(self.ones[ten])
        return ' '.join([x for x in ans if x.strip()])
    
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        s, ans = str(num)[::-1], []
        for i in range(0, len(s), 3):
            part = int(s[i:i+3][::-1])
            if i and part:
                ans.append(self.thou[i//3])
            ans.append(self.section(part))
        return ' '.join([x for x in ans[::-1] if x.strip()])
        
        