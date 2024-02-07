class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        mins = []
        for i in range(len(heights)):
            t = (heights[i], names[i])
            mins.append(t)
        mins.sort(reverse = True)
        names2 = [i[1] for i in mins]
        return names2
        
