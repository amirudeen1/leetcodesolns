class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i, num in enumerate(nums):
            if (target - num) in hash.keys():
                return [hash[target - num], i]
            hash[num] = i
