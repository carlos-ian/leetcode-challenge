class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        last_word = words[-1]
        size = len(last_word)
        return size