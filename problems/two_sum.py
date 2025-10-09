class Solution(object):
    def twoSum(self, nums, target):
        sol = [0, 0]

        for i in range(len(nums)):
            for a in range(len(nums)):
                if i != a and nums[i] + nums[a] == target:
                    sol[0] = i
                    sol[1] = a
                    return sol[0], sol[1]