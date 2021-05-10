# -*- coding: utf-8 -*-

# 快速排序：对 arr 中 l 到 r 位进行排序
# arr : 待排序数组
# left   : 待排序区间起始坐标
# right   : 待排序区间结束坐标
def quick_sort(arr, left, right):
    if left >= right:
        return

    # 选取基准值，基准值位置先空出来，用于放置违反规则的值
    ref = arr[left]

    left_index, right_index = left, right
    while left_index < right_index:
        # 从右向左扫，直到扫到右边的值小于基准值
        while left_index < right_index and arr[right_index] >= ref:
            right_index -= 1
        # 此时left_index（基准值）位置是空出来的，右侧违反规则的值放到left_index处
        if left_index < right_index:
            arr[left_index] = arr[right_index]

        # 从左向右扫，直到扫到左边的值大于基准值
        while left_index < right_index and arr[left_index] <= ref:
            left_index += 1
        # 上一步的操作right_index的值已经移动到左侧，此时将左侧大于基准值的值放到right_index
        if left_index < right_index:
            arr[right_index] = arr[left_index]

    # 最后空出来的位置放入基准值
    arr[left_index] = ref
    quick_sort(arr, left, left_index - 1)
    quick_sort(arr, left_index + 1, right)


if __name__ == '__main__':
    nums = [5, 1, 3, 4, 9, 6, 2, 7, 0, 8]
    quick_sort(nums, 0, 9)
    print(nums)
