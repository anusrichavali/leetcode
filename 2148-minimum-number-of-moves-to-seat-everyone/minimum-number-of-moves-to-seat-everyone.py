class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        s = 0
        for i in range(len(seats)):
            s += abs(seats[i] - students[i])
        return s

        