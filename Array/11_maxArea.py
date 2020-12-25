from typing import List
#解法1：暴力解，两次循环，计算所有线的面积，然后输出最大的

#解法2：双指针。
# 面积 = 短线长度 * 两条线长度
# 要想面积最大，只需要移动短线，直到两条线重合
class Solution:
    def maxArea(self, height: List[int]) -> int:
        header = 0
        tailer = len(height)-1
        maxArea = 0
        while header != tailer:
            if height[header] > height[tailer]:
                tempMaxArea = height[tailer] * (tailer-header)
                tailer -= 1
            else:
                tempMaxArea = height[header] * (tailer - header)
                header += 1
            if tempMaxArea > maxArea:
                maxArea = tempMaxArea
        return maxArea

if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))