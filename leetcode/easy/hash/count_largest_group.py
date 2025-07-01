class CountLargestGroup:
    """
    Leetcode #1399
    Link: https://leetcode.com/problems/count-largest-group/description/
    """

    def count_largest_group(self, n: int) -> int:
        stats = dict()
        for i in range(1, n + 1):
            p = 0
            for d in str(i):
                p = p + int(d)
            stats[p] = 1 + (0 if p not in stats else stats[p])

        c = 0
        m = -1
        for v in stats.values():
            if v > m:
                c, m = 1, v
            elif v == m:
                c = c + 1
        return c
