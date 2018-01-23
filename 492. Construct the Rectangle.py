class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        for w in range(int(math.sqrt(area)), 0, -1):
            l = int(area / w)
            if l * w == area:
                return [l, w]
