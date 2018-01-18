class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        res = i = j = 0
        while True:
            if j >= len(houses):
                break
            if houses[j] <= heaters[i]:
                res = max(heaters[i] - houses[j], res)
                j += 1
                continue
            if i + 1 >= len(heaters):
                res = max(houses[j] - heaters[i], res)
                j += 1
                continue
            if houses[j] - heaters[i] > heaters[i + 1] - houses[j]:
                res = max(heaters[i + 1] - houses[j], res)
                i += 1
                continue
            else:
                res = max(houses[j] - heaters[i], res)
            j += 1
        return res


if __name__ == '__main__':
    houses = [474833169, 264817709, 998097157, 817129560]
    heaters = [197493099, 404280278, 893351816, 505795335]
    s = Solution()
    print(s.findRadius(houses, heaters))
