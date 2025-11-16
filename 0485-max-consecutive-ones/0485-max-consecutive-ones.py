class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0
        max = count
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=1
                if max < count:
                    max = count
            else:
                count =0
        return max