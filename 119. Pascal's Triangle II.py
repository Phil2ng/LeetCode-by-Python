class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0: return [];
        res = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            res[i] = 1
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
