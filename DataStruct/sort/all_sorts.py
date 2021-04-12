# -*- coding:utf-8 -*-
# @FileName  :all_sort.py
# @Time      :2021/3/22 16:08
# @Author    :Haozr
from typing import List


# 排序算法
class Solution:
    def select_sort(self,nums:List[int]):
        """选择排序 选择一个最小的数调换到第一个位置"""
        n = len(nums)
        for i in range(n):
            #print(nums)
            min = i
            for j in range(i+1,n):
                if nums[j] < nums[min]:
                    min = j
            if min != i:
                nums[i],nums[min] = nums[min],nums[i]

    def bubble_sort(self,nums:List[int]):
        """冒泡排序 每两个数比较，顺序不对就对换，即大的往后，小的往前"""
        n = len(nums)
        for i in range(n-1, 0, -1):
            print(nums)
            for j in range(n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        return nums

    def bubble_sort_1(self,nums:List[int]):
        """ 优化1：（整体有序）设置一个标志，如果一趟比较下来，没有位置发生交换，说明已经排好序"""
        n = len(nums)
        flag = 0
        for i in range(0, n -1):
            flag = 0
            print(nums)
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = 1
            if flag == 0:
                return nums
        return nums

    def bubble_sort_2(self,nums:List[int]):
        """ 优化2：（后边有序）每趟排序记下最后交换的位置，下趟排序比较到上次标记的位置"""
        n = len(nums)
        flag = 0
        end = n - 1
        k = 0
        for i in range(n-1):
            flag = 0
            print(nums,end,k)
            for j in range(end):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    k = j + 1
                    flag = 1
            if flag == 0:
                return nums
            end = k
        return nums

    def bubble_sort_3(self,nums:List[int]):
        """冒泡排序 优化3：在2的基础上可以在每趟排序结束后，添加一个反向循环，确定最小值"""
        n = len(nums)
        flag = 0
        k = 0
        end = n - 1
        for i in range(n -1):
            flag = 0
            print(nums)
            for j in range(end):
                if nums[j]> nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    k = j + 1
                    flag = 1
            if flag == 0:
                return nums
            end = k
            flag = 0
            for j in range(end,0,-1):#反向循环，确定最小值
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    falg = 1
            if flag == 0:
                return nums
        return nums

    def insert_sort(self,nums:List[int]):
        """插入排序 按顺序把数插入到前面有序部分"""
        n = len(nums)
        for i in range(1,n):
            temp = nums[i]
            print(temp,nums)
            j = i -1
            while j >= 0 and temp < nums[j]:#从后往前遍历有序部分
                print(j,nums[j])
                nums[j+1] = nums[j]#把大于temp的数都往后移一位
                j -= 1
            nums[j+1] = temp
        return nums

    def merge_sort(self,nums:List[int]):
        """归并排序 """
        def merge(left,right):
            """合并子表"""
            result = []
            i,j = 0,0
            m,n = len(left),len(right)
            while i < m and j < n:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            return result + left[i:]+right[j:]
        n = len(nums)
        if n <= 1:
            return nums
        left = self.merge_sort(nums[:n//2])#划分子表
        right = self.merge_sort(nums[n//2:])
        return merge(left,right)

    def quick_sort(self,nums:List[int]):
        """快速排序 把数组分为左右两部分，然后再对左右两部分继续分，直到子数组等于1 """
        def quick(left,right):
            if left >= right:
                return
            low = left
            high = right
            key = nums[low]
            print("**",nums)
            while low < high:
                print(low,high,nums[low],nums[high],nums)
                while key <= nums[high] and low < high:#找到右边小于key
                    high -= 1
                nums[low] = nums[high]
                while key > nums[low] and low < high:#找到左边大于等于key
                    low += 1
                nums[high] = nums[low]
            print(low, high, nums[low], nums[high], nums)
            nums[high] = key
            quick(left,low-1)
            quick(low+1,right)
        quick(0,len(nums)-1)
        return nums

    def shell_sort(self,nums:List):
        """希尔排序 选择一个步长序列，按照步长分组，对每组进行插入排序"""
        n = len(nums)
        s = n // 2
        while s >= 1:#步长
            print(nums,s)
            for k in range(s):#遍历组 k为每组的第一个元素
                for i in range(s+k,n,s):#插入排序，遍历组内元素,从第二个开始遍历
                    j = i - s
                    temp = nums[i]
                    while j >= 0 and nums[j] > temp:#从后往前遍历
                        nums[j+s] = nums[j]
                        j = j - s
                    nums[j + s] = temp
            s //= 2
        return nums

    def heap_sort(self,nums:List[int]):
        """堆排序 增序 假设数组下标从1开始"""
        def adjust_heap(l,n):
            """从根节点root开始由上往下调整成大顶堆 arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2] """
            k = l * 2 + 1
            while k < n:
                if k + 1 < n and nums[k+1] > nums[k]:#是否有右结点，并大于左结点
                    k += 1
                if nums[k] > nums[l]:
                    nums[k], nums[l] = nums[l], nums[k]
                    l = k
                    k = l * 2 + 1
                else:
                    break
        n = len(nums)
        def build_heap():
            """建大顶堆"""
            for i in range(n//2 - 1, -1, -1):
                adjust_heap(i, n)
        build_heap()
        for i in range(n-1,0,-1):
            print(nums, i)
            nums[0],nums[i] = nums[i],nums[0]
            adjust_heap(0, i)
        return nums

    from functools import reduce
    def sum(self,nums:List):
        """不用循环求数组的和，用递归 或者用reduce(lambda a,b:a+b,nums)"""
        n = len(nums)
        def do_sum(i):
            if i < n:
                return nums[i] + do_sum(i+1)
            else:
                return 0
        return do_sum(0)

if __name__ == '__main__':
    s = Solution()
    nums = [49,38,65,97,76,13,27,49,109]
    nums1 = [65,38,97,76,13,27,49,8]
    nums2 = [4,2,2,6,7,8]
    print(s.heap_sort(nums1))
