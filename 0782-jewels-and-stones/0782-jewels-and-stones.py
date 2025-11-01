class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        length = 0
        for i in stones:
            for j in jewels:
                if i == j:
                    length += 1
                    break
        return length