class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pos_speed = sorted([(position[i], speed[i]) for i in range(len(position))])
        stack = []
        for i in range(len(pos_speed) - 1, -1, -1):
            time = (target - pos_speed[i][0])/float(pos_speed[i][1])
            stack.append(time)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
            
        