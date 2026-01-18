class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        n = sorted(nums)
        for i in range(len(n)):
            if n[i] not in d : 
                d[n[i]] = i 
        res = []
        for i in nums:
            res.append(d[i])
        return res 

            


        