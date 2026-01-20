class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                if maxi<count:
                    maxi = count
                count=0
        if maxi<count:
            maxi = count       
        return maxi

        