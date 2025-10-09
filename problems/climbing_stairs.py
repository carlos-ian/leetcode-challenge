class Solution:
    def climbStairs(self, n):
        stairs_ant = 1
        stairs_pos = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            for i in range(n-1):
                stairs_ant, stairs_pos = stairs_pos, stairs_ant + stairs_pos
            return stairs_pos