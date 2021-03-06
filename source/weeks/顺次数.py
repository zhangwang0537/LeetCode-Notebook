# 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
#
# 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
#
#  
#
# 示例 1：
#
# 输出：low = 100, high = 300
# 输出：[123,234]
# 示例 2：
#
# 输出：low = 1000, high = 13000
# 输出：[1234,2345,3456,4567,5678,6789,12345]
# 直接穷举
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        d = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,
             1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,
             123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        res = []
        for i in d:
            if low <= i <= high:
                res.append(i)
        return res
# 时间复杂度：O(1)，遍历一遍数组d，时间固定
# 空间复杂度：O(N)额外使用了数组