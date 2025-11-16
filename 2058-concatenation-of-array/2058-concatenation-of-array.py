class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = []
        for i in range(2):
            n.extend(nums)
        return n