class Solution(object):
    def romanToInt(self, s):
        value = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        result = 0
        last = 0
        for ch in reversed(s):
            num = value[ch]
            if num < last:
                result -= num
            else:
                result += num
            last = num

        return result
