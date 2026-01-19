class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            curr = target-nums[i]
            if curr in d:
                return [d[curr],i]
            d[nums[i]]=i
       
        