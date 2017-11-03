class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        i = 0
        c = 0b1
        tmp = x ^ y
        result = 0
        while i < 32:
            if tmp & c > 0:
                result += 1
            i += 1
            c <<= 1
        return result