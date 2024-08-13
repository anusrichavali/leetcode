class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] == 2:
                counts.pop(i)
        return list(counts)[0]