# -*- coding:utf-8 -*-
# @FileName  :42_trapping-rain-water.py
# @Time      :2020/12/28 16:25
# @Author    :Haozr
from typing import List


# 解法1：【双指针】积水高度由数值小的一边决定
#定义左右各一个指针，并定义左右两边最大高度，
#左右指针，哪个值小，哪个移动
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lmax,rmax = 0,0
        ans = 0
        while(l < r):
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    ans += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    ans += rmax - height[r]
                r -= 1
        return ans
#解法2：暴力解 对于每个高度i，形成的积水面积等于min(max[0:i],max[i:n])-i;
# 即每个桶与左右两边较底的桶形成水池，水池面积为两个桶的高度差*1
if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height1 = [4, 2, 0, 3, 2, 5]
    print(Solution().trap(height1))
