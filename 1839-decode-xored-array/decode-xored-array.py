class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [0] * (len(encoded) + 1)
        arr[0] = first
        for i in range(len(encoded)):
            arr[i + 1] = arr[i] ^ encoded[i]
        return arr
        