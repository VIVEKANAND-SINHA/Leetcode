
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        res = -1
        if n == 1:
            return 1
        while low <= high:
            mid = low + (high-low)//2
            if isBadVersion(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
