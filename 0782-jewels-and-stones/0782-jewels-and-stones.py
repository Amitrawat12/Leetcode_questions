class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        length =0

        for i in jewels:
            for j in stones:
                if i ==j:
                    length+=1
        return length