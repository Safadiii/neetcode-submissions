class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        if digits[-1] == 9:
            for digit_idx in range(len(digits) -1, -1, -1):
                if digit_idx == 0 and digits[digit_idx] == 9:
                    digits[digit_idx] = 0
                    digits.insert(0, 1)
                    return digits
                if digits[digit_idx] == 9:
                    digits[digit_idx] = 0
                else:
                    digits[digit_idx] += 1
                    break
        return digits
        