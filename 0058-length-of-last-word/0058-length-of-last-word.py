class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length =0
        maxi = 0

        s= s.split()
       
        return len(s[-1])