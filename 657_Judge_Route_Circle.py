class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for m in moves:
            if m == "R":
                x += 1
            elif m == "L":
                x -= 1
            elif m == "U":
                y += 1
            elif m == "D":
                y -= 1
            
        return x == 0 and y == 0