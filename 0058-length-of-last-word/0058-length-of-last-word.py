class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length =0
        maxi = 0
        c=0
        for i in s:
            if i == " ":
                
                length = 0
            else:
                length+=1
            c=length
            if c !=0:
                maxi=c

        return maxi