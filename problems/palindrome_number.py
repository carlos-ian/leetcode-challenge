class Solution(object):
    def isPalindrome(self, x):
        last_digit = 0
        inverted = 0
        number = x

        if (x < 0):
            return False
        elif (x == 0):
            return True
        elif (x > 0):
            while (x > 0):
                last_digit = x % 10
                inverted = inverted * 10 + last_digit
                x = x // 10 
            if (inverted == number):
                return True
            elif (inverted != number):
                return False
