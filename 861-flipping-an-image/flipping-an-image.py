class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = []
        for i in image:
            new_i = []
            for j in i:
                if j == 0:
                    new_i.insert(0, 1)
                else:
                    new_i.insert(0, 0)
            n.append(new_i)
        return n