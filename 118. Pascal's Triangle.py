class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return [];
        temp = [0, 1]
        res = []
        for i in range(numRows):
            rowList = []
            for j in range(len(temp) - 1):
                rowList.append(temp[j] + temp[j + 1])
            res.append(rowList)
            temp = rowList[:]
            temp.insert(0, 0)
            temp.append(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
