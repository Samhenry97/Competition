class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits)-1, -1, -1):
            digits[i] += int(carry)
            if digits[i] == 10:
                digits[i] = 0
                carry = True
            else:
                carry = False
        return ([1] if carry else []) + digits