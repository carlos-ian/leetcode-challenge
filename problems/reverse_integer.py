class Solution(object):
    def reverse(self, x):
        sinal = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        if reverse * sinal > 2147483648 or reverse * sinal < 2147483647 * -1:
            return 0
        else:   
            return reverse * sinal