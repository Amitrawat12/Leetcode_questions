class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = set()
        result = []
        left = 0
        maxi =0
        for right in range(len(s)):
            while s[right] in new:
                new.remove(s[left])
                left+=1
            new.add(s[right])
            maxi = max(maxi,right-left+1)
        return maxi

            
        