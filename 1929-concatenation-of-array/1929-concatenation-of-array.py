class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        n = len(nums)
        while i< n:
            nums.append(nums[i])
            i+=1
        return nums