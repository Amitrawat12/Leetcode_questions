class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # length = 0
        # for i in stones:
        #     for j in jewels:
        #         if i == j:
        #             length += 1
        #             break
        # return length

        jset = set(jewels)
        return sum(1 for c in stones if c in jset)