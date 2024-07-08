class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # char count frequency, 2 dicts, compare
        if len(s) != len(t):
            return False
        
        sCount = {}
        tCount = {}
        for i in s:
            sCount[i] = sCount.get(i, 0) + 1
        for i in t:
            tCount[i] = tCount.get(i, 0) + 1
        return sCount == tCount
