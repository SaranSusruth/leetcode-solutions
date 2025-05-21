class Solution(object):
    def isPalindrome(self, x):
        temp = x
        rev = 0
        while(temp>0):
            rem = temp % 10
            rev = rev * 10 + rem
            temp = temp // 10
        if num == rev:
            return True
        else:
            return False
num=int(input("enter the number to check:"))
s = Solution()
print(s.isPalindrome(num))