class Solution(object):
    def isPalindrome(self, x):
        reverseNum = 0
        tempOriginal = x

        while(tempOriginal > 0):
            lastDigit = tempOriginal % 10
            reverseNum = reverseNum * 10 + lastDigit
            tempOriginal = tempOriginal / 10

        if(x == reverseNum):
            return True
        else:
            return False
        