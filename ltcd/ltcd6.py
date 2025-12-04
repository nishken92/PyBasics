class Solution:
    def longestCommonPrefix(self, strs):
        out = ""
        l = len(strs)
        for i in range(0,l):